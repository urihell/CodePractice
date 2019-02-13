import boto3
from botocore.exceptions import ClientError
import os
import pandas as pd
import json
from tqdm import tqdm
import argparse


def hook(t):
    def inner(bytes_amount):
        t.update(bytes_amount)

    return inner


class Xrefmerge:

    def __init__(self, bucket_name='connector-hub-xref-dev', prefix='xref/in/account/474/job/',
                 dest_path='/Users/urieldabby/Documents/tmp/', cust_filename='n_job_id.csv', merged_csv='merge.csv'):
        self.dest_path = dest_path
        self.bucket_name = bucket_name
        self.prefix = prefix
        self.cust_filename = cust_filename
        self.merged_csv = merged_csv

        # Generate xref/in or xref/out CSV filename string
        if '/in/' in self.prefix:
            self.xref_file = 'xref_in.csv'
        elif '/out/' in self.prefix:
            self.xref_file = 'xref_out.csv'

        # Create CSV headers
        if '/job' in self.prefix:
            self.header1 = 'ext_job_id_o'
            self.header2 = 'dm_job_id'
            self.header3 = 'new_ext_job_id'
        elif '/organization' in self.prefix:
            self.header1 = 'ext_org_id_o'
            self.header2 = 'dm_org_id'
            self.header3 = 'new_ext_org_id'
        elif '/customer' in self.prefix:
            self.header1 = 'ext_cust_id_o'
            self.header2 = 'dm_cust_id'
            self.header3 = 'new_ext_cust_id'

    def update_local_dir(self):
        # Update local folder path
        os.chdir(self.dest_path)
        folder = os.getcwd()
        return folder

    def remove_hidden_files(self):
        # Checks for hidden files and remove if exists
        for root, dirs, files in os.walk(self.dest_path, topdown=False):
            for name in files:
                if name.startswith('.'):
                    hidden_path = os.path.join(root, name)
                    os.remove(hidden_path)
                    print("Hidden File %s Removed!\n" % name)

    def download_s3_files(self):
        # Downloads bucket files to the destination path
        print('Downloading files from %s/%s...\n' % (self.bucket_name, self.prefix))
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(self.bucket_name)
        files = bucket.objects.filter(Prefix=self.prefix)
        for obj in files:
            try:
                object = s3.Object(self.bucket_name, obj.key)
                obj_size = object.content_length
                with tqdm(total=obj_size, unit='B', unit_scale=True, desc=obj.key) as t:
                    s3.Bucket(self.bucket_name).download_file(obj.key, os.path.basename(obj.key), Callback=hook(t))
            except ClientError as e:
                raise

    def create_xref_files(self):
        # Read /Documents/tmp/ folder and write to a CSV file
        self.remove_hidden_files()
        print('Reading XREF files and Writing to a CSV file\n')
        xref_list = []
        for file in os.listdir(self.dest_path):
            if file not in [self.cust_filename, self.merged_csv, self.xref_file, 'NEW_XREF_FILES']:
                with open(file, 'r') as xref:
                    read = xref.read()
                    xref_list.append([file, read])
        xref_df = pd.DataFrame(xref_list)
        if '/in/' in self.prefix:
            xref_df.to_csv(self.xref_file, index=False, header=[self.header1, self.header2])
        elif '/out/' in self.prefix:
            xref_df.to_csv(self.xref_file, index=False, header=[self.header2, self.header1])
        print('%s file written successfully' % self.xref_file)

    def merge_csv(self):
        # Merge CSV 1 with CSV 2 and create a new merge.csv file
        try:
            print('Reading Files...\n')
            df1 = pd.read_csv(self.xref_file, index_col=False)
            if '/out/' in self.prefix:
                df1[self.header1] = df1[self.header1].str.split('"').str[1]
            if '/in/' in self.prefix:
                df1[self.header2] = df1[self.header2].str.split('[').str[1]
                df1[self.header2] = df1[self.header2].str.split(']').str[0]
            df2 = pd.read_csv(self.cust_filename, index_col=False)
        except:
            print('Failed to Read Files\n')
        try:
            df3 = pd.merge(df1, df2)
            print(df3)
            df3.to_csv(self.merged_csv, sep=',', index=False)
            print('%s file written successfully\n' % self.merged_csv)
        except:
            print('Failed to Merge Files\n')

    def new_xref_files(self):
        self.remove_hidden_files()
        print('Writing Files to %sNEW_XREF_FILES' % self.dest_path)
        df3 = pd.read_csv(self.merged_csv)
        try:
            os.chdir('%sNEW_XREF_FILES' % self.dest_path)
        except:
            os.mkdir('%sNEW_XREF_FILES' % self.dest_path)
            os.chdir('%sNEW_XREF_FILES' % self.dest_path)
        try:
            for index, row in df3.iterrows():
                if '/in/' in self.prefix:
                    with open(row[self.header3], 'w') as xref_file:
                        xref_file.write(str(row[self.header2]))
                elif '/out/' in self.prefix:
                    with open(str(row[self.header2]), 'w') as xref_file:
                        external_ids = json.dumps([row[self.header3], row[self.header1]])

                        xref_file.write(str(external_ids))
            print("Files Written Successfully to %sNEW_XREF_FILES\n" % (self.dest_path))
        except:
            print('Unable To Write Files in %sNEW_XREF_FILES' % self.dest_path)
            raise

    def upload_to_s3(self):
        # try:
        print("Uploading Files to s3://%s/%s..." % (self.bucket_name, self.prefix))
        os.chdir('%s/NEW_XREF_FILES' % self.dest_path)
        self.remove_hidden_files()
        folder = os.getcwd()
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(self.bucket_name)

        try:
            for root, dirs, files in os.walk(folder, topdown=False):
                for name in files:
                    if not name.startswith('.'):
                        file_size = os.path.getsize(name)
                        with tqdm(total=file_size, unit_scale=True, desc='Uploading ' + name) as t:
                            bucket.upload_file(name, self.prefix + name, Callback=hook(t))
                print("\nNew XREF Files uploaded successfully to s3://%s/%s\n" % (self.bucket_name, self.prefix))
        except:
            print("Unable to Upload Files to s3://%s/%s" % (self.bucket_name, self.prefix))


def main():
    s3merge = Xrefmerge()
    s3merge.update_local_dir()
    s3merge.remove_hidden_files()
    s3merge.download_s3_files()
    s3merge.create_xref_files()
    s3merge.merge_csv()
    s3merge.new_xref_files()
    s3merge.upload_to_s3()


if __name__ == '__main__':
    main()
