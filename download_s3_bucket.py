from xref_csv_merge import Xrefmerge


s3merge = Xrefmerge(prefix='xref/in/account/474/job/')
s3merge.update_local_dir()
s3merge.remove_hidden_files()
s3merge.update_local_dir()
s3merge.download_s3_files()
s3merge.create_xref_files()
s3merge.merge_csv()
#
s3merge.new_xref_files()
s3merge.upload_to_s3()
