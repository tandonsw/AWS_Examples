#!/usr/bin/python
################################################################################
####
####  NAME:    sagemaker_restart_ni
####
####  PURPOSE: This Python-based AWS Lambda function will consume the Amazon Linux
####           RSS feed and restart all notebook instances if it finds a new patch
####           available for Amazon Linux.
####
####  USAGE:   sagemaker_restart_ni (Deployed on AWS with a monthly Cloudwatch schedule)
####
####
################################################################################
#
#  CHANGE HISTORY:
#
#  VERS  DATE         PGMR NAME         DESCRIPTION OF CHANGE
#  ----  -----------  -------------- -------------------------------------------
#  1.0   28-Nov-2018  Swapnil Tandon    Initial Version
#
################################################################################
#import the required modules
import boto3
import os
import feedparser
import datetime
import time
from dateutil.parser import parse as parse_date
from datetime import tzinfo, timedelta, datetime

ni_list=[]
amazon_linux_feed="https://alas.aws.amazon.com/alas.rss"
access_key='AKIAJX7ZTQSYKUJIE5KQ'
secret_key='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'
region='us-east-2'

#Define timezone for present date comparison and get current datetime
ZERO = timedelta(0)
class UTC(tzinfo):
  def utcoffset(self, dt):
    return ZERO
  def tzname(self, dt):
    return "UTC"
  def dst(self, dt):
    return ZERO
utc = UTC()
present = datetime.now(utc)

#Parse Amazon Linux feed
feed=feedparser.parse(amazon_linux_feed)

#Get the Last patch date and convert it to python datetime format
lastpatch=feed['entries'][0]['published']
lastpatchdate=parse_date(lastpatch)

patch_month=lastpatchdate.month
present_month=present.month
last_month=present_month-1

if(patch_month == last_month):
  client = boto3.client('sagemaker',region_name=region)
  response = client.list_notebook_instances(
    SortBy='Name',
    SortOrder='Ascending',
    StatusEquals='InService'
  )
  length_key = len(response['NotebookInstances'])
  for i in range(length_key):
    ni_list.append(response['NotebookInstances'][i]['NotebookInstanceName'])
  for ni in ni_list:
    stop_notebook = client.stop_notebook_instance(
      NotebookInstanceName=ni
    )
    while 1:
      try:
        response2= client.describe_notebook_instance(
          NotebookInstanceName=ni
        )
      except:
        continue
      if(response2['NotebookInstanceStatus'] == "Stopped"):
        break
    start_notebook = client.start_notebook_instance(
      NotebookInstanceName=ni
    )

