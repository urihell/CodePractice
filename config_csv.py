from config_service import ConfigClient as cc
import json
import csv

def extract_app_config(full_data):

    data = full_data
    parsed_data = json.loads(data)
    app_data = parsed_data['app']

    with open('AppConfig.csv', mode='w') as csv_file:
        fieldnames = ['Configuration', 'Value']
        writer = csv.writer(csv_file)
        writer.writerow(fieldnames)
        for config in app_data.items():
            writer.writerow(config)
    print ('App Configuration file created successfully')

def get_config():
    env_a = cc()
    env_a.environment_input()
    env_a.admin_token_input()
    env_a.account_input()
    env_a.entity_input()
    config = env_a.get_account_config()



# def string():
#     full_data = r"""
#
# {
# "app": {
#     "acceptTitle": "Accept",
#     "canAddAJob": false,
#     "canAddBillingItems": true,
#     "canAddEstimate": true,
#     "canAddInvoice": true,
#     "canAddLineItem": true,
#     "canAddPayment": true,
#     "canDeleteBillingDocuments": true,
#     "canDeleteBillingItems": true,
#     "canDeleteLineItem": true,
#     "canEditBillingItems": true,
#     "canEditProfile": true,
#     "canPauseAvailability": true,
#     "canReceiveReminders": false,
#     "canRescheduleJobs": true,
#     "canSaveLineItemForFuture": true,
#     "canSeeBilling": true,
#     "canSeeBillingDocumentNumber": true,
#     "canSeeBillingSettings": true,
#     "canSeeCantContactCustomer": false,
#     "canSeeContracts": true,
#     "canSeeCustomerEdit": false,
#     "canSeeCustomerPortalAttachmentDescriptionField": true,
#     "canSeeCustomerPortalAttachmentManufacturerField": true,
#     "canSeeCustomerPortalAttachmentModelField": true,
#     "canSeeCustomerPortalAttachmentUpload": true,
#     "canSeeDesktopSettings": true,
#     "canSeeIssueDate": true,
#     "canSeeMobileInbox": false,
#     "canSeeNoteEdit": true,
#     "canSeeNotes": true,
#     "canSeePONumber": true,
#     "canSeePaymentTerms": true,
#     "canSeeQuickbooks": false,
#     "canSeeRequestCallBack": false,
#     "canSeeResetToScheduled": false,
#     "canSeeStartDate": true,
#     "canSeeTaxes": true,
#     "canSeeTechnicianPhone": true,
#     "canSeeWorkBilling": true,
#     "canSelectMultiple": true,
#     "canSendByEmail": true,
#     "canSetAvailability": true,
#     "completeReasons": [
#         "service_provided|Service Provided|false|complete",
#         "unrepairable|Unrepairable|false|complete",
#         "declined_service|Declined Service|false|complete",
#         "referred_out|Referred Out|false|complete",
#         "waiting_on_parts|Waiting on Parts|false|paused",
#         "follow_up_with_customer|Follow Up Required|false|paused",
#         "no_show|Customer Not Home|false|paused",
#         "additional_tools_or_labor|Additional Tools or Labor|false|paused",
#         "cannot_contact_customer|Cannot Contact Customer|false|paused"
#     ],
#     "declineTitle": "Decline",
#     "hideAddressUntilAccepted": false,
#     "hideCustomerIfCanceled": false,
#     "hideCustomerUntilDayOf": false,
#     "hideCustomerUntilScheduled": false,
#     "hideFilterTechnicians": false,
#     "hideJobDetailsUntilAccepted": false,
#     "hideSchedulePageMap": false,
#     "integrations": [
#         "American Home Shield|https://files-api-dev.dispatch.me/v1/datafiles/0e3601b9-5a4b-4692-b82d-502f61107876/proportional_250|Learn More|AHS",
#         "Test New Source|https://img-dispatch.s3.amazonaws.com/guides/magnify.png|Learn More|mkt-newsource|Job Sources",
#         "Wintac|https://img-dispatch.s3.amazonaws.com/marketplace/wintac.jpg|Coming Soon|mkt-wintac|Connections",
#         "HomeAdvisor|https://img-dispatch.s3.amazonaws.com/marketplace/homeadvisor.jpg|Learn More|mkt-homeadvisor|Job Sources",
#         "Networx|https://img-dispatch.s3.amazonaws.com/marketplace/networx.png|Learn More|mkt-networx|Job Sources",
#         "Customer Booking Page|https://img-dispatch.s3.amazonaws.com/marketplace/bookingpage.png|Get My Link|mkt-bookingpage|Job Sources"
#     ],
#     "jobTrackerCanReschedule": true,
#     "jobTrackerCanSelectMultipleRatingReasons": true,
#     "jobTrackerRatingReasons": [
#         "Technician Service",
#         "Timeliness",
#         "Price",
#         "Quality"
#     ],
#     "jobTrackerShowRatingReasons": true,
#     "mustMatchBillingItemList": false,
#     "privateNotes": true,
#     "readOnlyCustomerInformation": false,
#     "showDeclineButton": true,
#     "showPrivateNotesToggle": true,
#     "showSuggestedTimes": true,
#     "showWarrantyRating": false,
#     "suggestedTimesStartDateOffset": 2,
#     "useAppointmentWindows": true,
#     "showCustomerPortalRatingPage": true,
#     "canAcceptDraftAppointment": true,
#     "canSeeBrandedEmails": true,
#     "canSeeServiceInstructions": false,
#     "cancelReasons": [
#         "customer_cancelled|Customer Cancelled|false|canceled",
#         "issues_resolved_without_service_visit|Issues Resolved Without Service Visit|false|canceled",
#         "decided_against_repair_without_service_visit|Decided Against Repair Without Service Visit|false|canceled"
#     ],
#     "customForms": [
#         "equipment:Equipment|make:Make|model:Model|serialNumber:Serial Number|age:Age (Years)|diagnosis:Diagnosis"
#     ],
#     "jobTrackerRequireAdditionalComments": false,
#     "rejectReasons": [
#         "Area Not Covered",
#         "Cannot Complete Job",
#         "No Capacity",
#         "Other (Call Sub Zero call center)"
#     ],
#     "reports": [
#         "94723|Your Jobs|daterange",
#         "94678|Your Reviews|daterange",
#         "94711|Your Technicians|daterange",
#         "101123|Your Billing|daterange"
#     ]
# },
# "notifications": {
#     "email": {
#         "events": {
#             "appointment__assigned": {
#                 "condition": null,
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "appointment__canceled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "appointment__complete": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "appointment__created": {
#                 "condition": null,
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "appointment__draft": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "appointment__enroute": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "appointment__notify_rescheduled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "appointment__reassigned": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "appointment__rescheduled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "appointment__scheduled": {
#                 "templates": {
#                     "body": "[DEFAULT] New appointment scheduled to technician",
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "appointment__started": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "appointment__suggested_times__customer_created": {
#                 "condition": null,
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": null
#             },
#             "appointment__unassigned": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job__canceled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job__closed": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job__complete": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job__created": {
#                 "templates": {
#                     "body": "[Aggregator2] Job Created to Dispatcher",
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "always"
#             },
#             "job__created_by_account": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job__draft": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job__paused": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job__rejected": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job__scheduled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job__unscheduled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job_offer__accepted": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__canceled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__created": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__entity_accepted": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__entity_canceled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__entity_expired": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__entity_offered": {
#                 "templates": {
#                     "body": "[Aggregator] New Job Offer (AWE)",
#                     "subject": null
#                 },
#                 "when": "never",
#                 "condition": "data.organization.usage_mode !== 'ghost'"
#             },
#             "job_offer__entity_rejected": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__entity_reoffer": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__expired": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__offered": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__rejected": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "organization__created": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "organization__setup_complete": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "payment__created": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "survey_response__created": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "survey_response__send": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "survey_response__submitted": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "survey_response__updated": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "user__created": {
#                 "templates": {
#                     "body": "[Default] A new account was made for you on Dispatch",
#                     "subject": null
#                 },
#                 "when": "always",
#                 "condition": "data.organization.usage_mode !== 'ghost'"
#             },
#             "user__email_password_reset": {
#                 "condition": null,
#                 "templates": {
#                     "body": "reset-password",
#                     "subject": null
#                 },
#                 "when": "always"
#             },
#             "job_offer__notify_organization": {
#                 "condition": "data.organization.usage_mode !== 'ghost'",
#                 "templates": {
#                     "body": "[Aggregator] External event email"
#                 },
#                 "when": "always"
#             },
#             "survey_response__five_star": {
#                 "condition": "data.organization.usage_mode !== 'ghost'",
#                 "templates": {
#                     "body": "Positive Review with Profile Builder Advertisement"
#                 },
#                 "when": "always"
#             },
#             "survey_response__four_star": {
#                 "condition": "data.organization.usage_mode !== 'ghost'",
#                 "templates": {
#                     "body": "Positive Review with Profile Builder Advertisement"
#                 },
#                 "when": "always"
#             },
#             "attachment__created_by_customer": {
#                 "templates": {}
#             },
#             "job__message_replied": {
#                 "templates": {
#                     "body": "sms-reply-notification",
#                     "subject": "{{customer.full_name}} Sent you a Message in Dispatch.me"
#                 },
#                 "when": "always"
#             },
#             "job__notify_organization": {
#                 "templates": {
#                     "body": "[Aggregator] External event email"
#                 },
#                 "when": "always"
#             },
#             "organization__message_received": {
#                 "templates": {
#                     "body": "customer-message-notification-to-dispatcher"
#                 },
#                 "when": "always"
#             },
#             "user__created_default": {
#                 "when": "always"
#             }
#         }
#     },
#     "robocall": {
#         "events": {
#             "appointment__assigned": {
#                 "condition": null,
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": null
#             },
#             "appointment__created": {
#                 "condition": null,
#                 "metricTags": [
#                     "tasdf"
#                 ],
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": null
#             },
#             "appointment__suggested_times__customer_created": {
#                 "condition": null,
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": null
#             },
#             "organization__created": {
#                 "config": {
#                     "input": [
#                         {
#                             "action": "action",
#                             "event": "event",
#                             "number": 1
#                         },
#                         {
#                             "action": "action",
#                             "event": "event",
#                             "number": 2
#                         }
#                     ],
#                     "onAnswer": {
#                         "play": "Play",
#                         "say": "Say"
#                     },
#                     "onInput": {
#                         "play": "PLay",
#                         "say": "Say"
#                     }
#                 },
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "always"
#             },
#             "user__email_password_reset": {
#                 "condition": null,
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": null
#             }
#         }
#     },
#     "sms": {
#         "events": {
#             "appointment__assigned": {
#                 "condition": null,
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "appointment__canceled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "appointment__complete": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "appointment__created": {
#                 "condition": null,
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "appointment__draft": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "appointment__enroute": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "appointment__notify_rescheduled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "appointment__reassigned": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "appointment__rescheduled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "appointment__scheduled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "appointment__started": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "appointment__suggested_times__customer_created": {
#                 "condition": null,
#                 "templates": {
#                     "body": "fg",
#                     "subject": null
#                 },
#                 "when": null
#             },
#             "appointment__unassigned": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job__canceled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job__closed": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job__complete": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job__created": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job__created_by_account": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job__draft": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job__paused": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job__rejected": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job__scheduled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job__unscheduled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "job_offer__accepted": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__canceled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__created": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__entity_accepted": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__entity_canceled": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__entity_expired": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__entity_offered": {
#                 "templates": {
#                     "body": "You have a new job offer from {{account.title}}. Open the Dispatch app to view the job details.",
#                     "subject": null
#                 },
#                 "when": "never",
#                 "condition": "data.organization.usage_mode !== 'ghost'"
#             },
#             "job_offer__entity_rejected": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__entity_reoffer": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__expired": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__offered": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "job_offer__rejected": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "organization__created": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "organization__setup_complete": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "payment__created": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "survey_response__created": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "survey_response__send": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": "never"
#             },
#             "survey_response__submitted": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "survey_response__updated": {
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "timing": {
#                     "delay": 0,
#                     "timeout": 0
#                 },
#                 "when": "never"
#             },
#             "user__created": {
#                 "templates": {
#                     "body": "Welcome to Dispatch! To install the app, go to {{urls.get}} from your mobile device.",
#                     "subject": null
#                 },
#                 "when": "always",
#                 "condition": "data.organization.usage_mode !== 'ghost' && data.organization.signup_source !== null"
#             },
#             "user__email_password_reset": {
#                 "condition": null,
#                 "templates": {
#                     "body": null,
#                     "subject": null
#                 },
#                 "when": null
#             },
#             "job_offer__notify_organization": {
#                 "condition": "data.organization.usage_mode !== 'ghost'",
#                 "templates": {
#                     "body": "{{eventData.text}}"
#                 },
#                 "when": "always"
#             },
#             "job__message_replied": {
#                 "templates": {
#                     "body": "Message Replied"
#                 },
#                 "when": "always"
#             },
#             "job__notify_organization": {
#                 "templates": {
#                     "body": "{{eventData.text}}"
#                 },
#                 "when": "always"
#             },
#             "job__service_instructions_updated": {
#                 "templates": {}
#             },
#             "user__created_default": {
#                 "templates": {
#                     "body": "Welcome new user {{user.first_name}}"
#                 },
#                 "when": "always"
#             }
#         }
#     },
#     "webhook": [],
#     "push": {
#         "events": {
#             "appointment__assigned": {
#                 "when": "never"
#             },
#             "organization__message_received": {
#                 "templates": {
#                     "body": "{{messageContent}}",
#                     "page": "MessageListPage",
#                     "pageOptions": "{\n  \"test\": \"test\"\n}",
#                     "subject": "{{customer.full_name}}"
#                 },
#                 "when": "always"
#             },
#             "survey_response__five_star": {
#                 "when": "always"
#             }
#         }
#     }
# }
# }"""
#     return full_data

def main():
    full_data = string()
    extract_app_config(full_data)

main()


