#!/usr/bin/python
import os

# Class funcs will have:
# -Name
# -Author
# -Sophistication
# -Info

# Required Options for the class

class TemplateModule:

  def __init__(self):
    # Meta Tags for file name and such:
    self.OutputName = "TelecommuteOpportunities.mht"
    self.RenderName = "TelecommuteOpportunities.mht"
    self.CoreOptions = "[Text, Html, Link]"
    # Required for each class:
    self.Name = "Increased on opportunities for employees to telecommute."
    self.Author = "Killswitch-GUI"
    self.Type = "Html"
    self.Info = """A very targeted email to corps that would support Telecommute options
                    in the first place. Telling users the increased opportunities for employees 
                    to telecommute can be effective to entice users act fast."""
    self.Sophistication = "High" 
    self.SampleImage = str('''Modules/Sample/TelecommuteOpportunities.png''')
    self.TemplatePath = str('''Modules/EmailTemplates/TelecommuteOpportunities.email''')
    # Required options for itself:
    self.RequiredOptions = {
                              "FromEmail" : ["noreply@agency.com", "From Email"],
                              "FromName" : ["Alex Jason", "From Full Name"],
                              "TargetCompany" : ["Cyber Power", "Set the Target Company Full Name" ],
                              "TargetLink" : ["%URL%", "The full path link"],
                              "CurrentQuater" : ["Q1", "Current Fiscal Quater"],
                              "DueDate" : ["Sep 01, 2016", "The Due Date of the Form"],
                              "NotificationDate" : ["Sep 01, 2016", "Notify of acceptance"],

                            }
  def Generate(self, filename, location, Verbose=False):
    # Gen will get 
    # Filename = the name of the output
    # Location = Where do you want to place the output
    # Verbose = Print all help data
    # adapted from Andy
    replaceDict = {
      'FROM_EMAIL' : self.RequiredOptions["FromEmail"][0],
      'FROM_NAME'    : self.RequiredOptions["FromName"][0],
      'TARGET_COMP_NAME' : self.RequiredOptions["TargetCompany"][0],
      'TARGET_LINK'    : self.RequiredOptions["TargetLink"][0],
      'CUR_QUATER'    : self.RequiredOptions["CurrentQuater"][0],
      'DUE_DATE'    : self.RequiredOptions["DueDate"][0],
      'NOTIFICATION_DATE': self.RequiredOptions["NotificationDate"][0],
      }
    WritePath =  str(filename) + str(location)

    with open(self.TemplatePath, 'r') as templateEmail:
      outputEmail = templateEmail.read()

    for dummy, value in replaceDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)
    try:
      f = open(WritePath, 'w')
      f.write(outputEmail)
      f.close
    except Exception as e:
      print e

  def Render(self, Verbose=False):
    # Gen will get 
    # Filename = the name of the output
    # Location = Where do you want to place the output
    # Verbose = Print all help data
    # adapted from Andy
    replaceDict = {
      'FROM_EMAIL' : self.RequiredOptions["FromEmail"][0],
      'FROM_NAME'    : self.RequiredOptions["FromName"][0],
      'TARGET_COMP_NAME' : self.RequiredOptions["TargetCompany"][0],
      'TARGET_LINK'    : self.RequiredOptions["TargetLink"][0],
      'CUR_QUATER'    : self.RequiredOptions["CurrentQuater"][0],
      'DUE_DATE'    : self.RequiredOptions["DueDate"][0],
      'NOTIFICATION_DATE': self.RequiredOptions["NotificationDate"][0],
      }

    with open(self.TemplatePath, 'r') as templateEmail:
      outputEmail = templateEmail.read()

    for dummy, value in replaceDict.iteritems():
        outputEmail = outputEmail.replace(dummy, value)
    return outputEmail
