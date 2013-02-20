# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Texternalerrors(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    loggedby = models.SmallIntegerField(null=True, db_column='LoggedBy', blank=True) # Field name made lowercase.
    receivedon = models.TextField(db_column='ReceivedOn', blank=True) # Field name made lowercase. This field type is a guess.
    errstatus = models.TextField(db_column='ErrStatus', blank=True) # Field name made lowercase.
    process = models.ForeignKey(Tprocess, null=True, db_column='Process', blank=True) # Field name made lowercase.
    issuedescr = models.TextField(db_column='IssueDescr', blank=True) # Field name made lowercase. This field type is a guess.
    employeeid = models.ForeignKey(Tmcbcemployee, null=True, db_column='EmployeeID', blank=True) # Field name made lowercase.
    errorbyparty = models.ForeignKey(Terrorparty, null=True, db_column='ErrorByParty', blank=True) # Field name made lowercase.
    errorbyperson = models.ForeignKey(Tmcbcemployee, null=True, db_column='ErrorByPerson', blank=True) # Field name made lowercase.
    resolution = models.TextField(db_column='Resolution', blank=True) # Field name made lowercase. This field type is a guess.
    affectedpayp = models.TextField(db_column='AffectedPayP', blank=True) # Field name made lowercase.
    incorrectpay = models.BooleanField(null=True, db_column='IncorrectPay', blank=True) # Field name made lowercase.
    relatedcase = models.IntegerField(null=True, db_column='RelatedCase', blank=True) # Field name made lowercase.
    impraction = models.TextField(db_column='ImprAction', blank=True) # Field name made lowercase. This field type is a guess.
    teamerr = models.TextField(db_column='TeamErr', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tExternalErrors'

class Tpeerchecking(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    relatedticket = models.IntegerField(null=True, db_column='relatedTicket', blank=True) # Field name made lowercase.
    auditor = models.IntegerField(null=True, db_column='Auditor', blank=True) # Field name made lowercase.
    datechecked = models.TextField(db_column='dateChecked', blank=True) # Field name made lowercase. This field type is a guess.
    dataentry = models.TextField(db_column='DataEntry', blank=True) # Field name made lowercase.
    processcorrect = models.TextField(db_column='ProcessCorrect', blank=True) # Field name made lowercase.
    sapcorrected = models.BooleanField(db_column='SAPCorrected') # Field name made lowercase.
    processcorrected = models.BooleanField(db_column='ProcessCorrected') # Field name made lowercase.
    completed = models.BooleanField(db_column='Completed') # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'tPeerchecking'

class Tversion(models.Model):
    ver = models.TextField(primary_key=True, db_column='Ver') # Field name made lowercase.
    class Meta:
        db_table = u'tVersion'

class Tmcbcemployee(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    forname = models.TextField(db_column='Forname', blank=True) # Field name made lowercase.
    surname = models.TextField(db_column='Surname', blank=True) # Field name made lowercase.
    payrollarea = models.TextField(db_column='PayrollArea', blank=True) # Field name made lowercase.
    eeid = models.IntegerField(null=True, db_column='EEID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tMCBCEmployee'

class Tsource(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    sourcename = models.TextField(db_column='SourceName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tSource'

class Tprocess(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    processname = models.TextField(db_column='ProcessName', blank=True) # Field name made lowercase.
    processtype = models.TextField(db_column='ProcessType', blank=True) # Field name made lowercase.
    letter = models.BooleanField(null=True, db_column='Letter', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tProcess'

class Tcurrentstatus(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    currentstatus = models.TextField(db_column='CurrentStatus', blank=True) # Field name made lowercase.
    clockstop = models.BooleanField(db_column='ClockStop') # Field name made lowercase.
    class Meta:
        db_table = u'tCurrentStatus'

class Tassignedto(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    assignedto = models.TextField(db_column='AssignedTo', blank=True) # Field name made lowercase.
    active = models.BooleanField(db_column='Active') # Field name made lowercase.
    class Meta:
        db_table = u'tAssignedTo'

class Tusrgroups(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    groupname = models.TextField(db_column='GroupName') # Field name made lowercase.
    class Meta:
        db_table = u'tUsrGroups'

class Tusringroups(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    usrid = models.ForeignKey(Tuser, null=True, db_column='UsrID', blank=True) # Field name made lowercase.
    usrgroup = models.ForeignKey(Tusrgroups, null=True, db_column='usrGroup', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tUsrInGroups'

class Tprocessassigment(models.Model):
    processid = models.ForeignKey(Tprocess, null=True, db_column='ProcessID', blank=True) # Field name made lowercase.
    groupid = models.ForeignKey(Tusrgroups, null=True, db_column='GroupID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tProcessAssigment'

class Tuser(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    username = models.TextField(db_column='UserName', blank=True) # Field name made lowercase.
    eeid = models.TextField(db_column='EeID', blank=True) # Field name made lowercase.
    passcode = models.TextField(db_column='PassCode', blank=True) # Field name made lowercase.
    userlvl = models.TextField(db_column='UserLvl', blank=True) # Field name made lowercase.
    active = models.BooleanField(null=True, db_column='Active', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tUser'

class Terrorparty(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    partyname = models.TextField(db_column='PartyName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tErrorParty'

class Ttracker(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    eeid = models.ForeignKey(Tmcbcemployee, null=True, db_column='EeID', blank=True) # Field name made lowercase.
    processid = models.ForeignKey(Tprocess, null=True, db_column='ProcessID', blank=True) # Field name made lowercase.
    casesubject = models.TextField(db_column='CaseSubject', blank=True) # Field name made lowercase.
    datereceived = models.TextField(db_column='DateReceived', blank=True) # Field name made lowercase. This field type is a guess.
    sourceid = models.ForeignKey(Tsource, null=True, db_column='SourceID', blank=True) # Field name made lowercase.
    multipleemployees = models.BooleanField(db_column='MultipleEmployees') # Field name made lowercase.
    multieenumber = models.SmallIntegerField(null=True, db_column='MultiEENumber', blank=True) # Field name made lowercase.
    pcrnumber = models.IntegerField(null=True, db_column='PCRNumber', blank=True) # Field name made lowercase.
    effectivedate = models.TextField(db_column='EffectiveDate', blank=True) # Field name made lowercase. This field type is a guess.
    expedite = models.BooleanField(db_column='Expedite') # Field name made lowercase.
    currentstatus = models.ForeignKey(Tcurrentstatus, null=True, db_column='CurrentStatus', blank=True) # Field name made lowercase.
    updatedate = models.TextField(db_column='UpdateDate', blank=True) # Field name made lowercase. This field type is a guess.
    comments = models.TextField(db_column='Comments', blank=True) # Field name made lowercase.
    assignedto = models.ForeignKey(Tassignedto, null=True, db_column='AssignedTo', blank=True) # Field name made lowercase.
    closedate = models.TextField(db_column='CloseDate', blank=True) # Field name made lowercase. This field type is a guess.
    timestart = models.TextField(db_column='TimeStart', blank=True) # Field name made lowercase. This field type is a guess.
    timestop = models.TextField(db_column='TimeStop', blank=True) # Field name made lowercase. This field type is a guess.
    tat = models.SmallIntegerField(null=True, db_column='TAT', blank=True) # Field name made lowercase.
    days_open = models.SmallIntegerField(null=True, db_column='Days_Open', blank=True) # Field name made lowercase.
    scanned = models.BooleanField(db_column='Scanned') # Field name made lowercase.
    indexed = models.BooleanField(db_column='Indexed') # Field name made lowercase.
    casedescription = models.TextField(db_column='CaseDescription', blank=True) # Field name made lowercase. This field type is a guess.
    requiredcompletiondate = models.TextField(db_column='RequiredCompletionDate', blank=True) # Field name made lowercase. This field type is a guess.
    incorrectrequest = models.BooleanField(db_column='IncorrectRequest') # Field name made lowercase.
    affectingpay = models.BooleanField(db_column='AffectingPay') # Field name made lowercase.
    clockstop = models.BooleanField(db_column='ClockStop') # Field name made lowercase.
    changelog = models.TextField(db_column='Changelog', blank=True) # Field name made lowercase.
    closedby = models.ForeignKey(Tuser, null=True, db_column='ClosedBy', blank=True) # Field name made lowercase.
    compareperiod = models.BooleanField(null=True, db_column='ComparePeriod', blank=True) # Field name made lowercase.
    inrejcomment = models.TextField(db_column='InRejComment', blank=True) # Field name made lowercase.
    lastupdate = models.TextField(db_column='LastUpdate', blank=True) # Field name made lowercase. This field type is a guess.
    excludefromsla = models.BooleanField(null=True, db_column='ExcludeFromSLA', blank=True) # Field name made lowercase.
    relatedticket = models.TextField(db_column='RelatedTicket', blank=True) # Field name made lowercase. This field type is a guess.
    manualpcr = models.BooleanField(null=True, db_column='ManualPCR', blank=True) # Field name made lowercase.
    personassigned = models.ForeignKey(Tuser, null=True, db_column='PersonAssigned', blank=True) # Field name made lowercase.
    payperiodstart = models.TextField(db_column='PayPeriodStart', blank=True) # Field name made lowercase.
    payperiodend = models.TextField(db_column='PayPeriodEnd', blank=True) # Field name made lowercase.
    paysliptrial = models.BooleanField(null=True, db_column='PaySlipTrial', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tTracker'

class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, unique=True)
    principal_id = models.IntegerField(unique=True)
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(null=True, blank=True)
    definition = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'sysdiagrams'

class Tchecklistsource(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    formname = models.TextField(db_column='FormName') # Field name made lowercase.
    sourcetablename = models.TextField(db_column='SourceTableName') # Field name made lowercase.
    class Meta:
        db_table = u'tChecklistSource'

class Tchecklistassigment(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    processid = models.ForeignKey(Tprocess, null=True, db_column='ProcessID', blank=True) # Field name made lowercase.
    formid = models.ForeignKey(Tchecklistsource, null=True, db_column='FormID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tChecklistAssigment'

class Trelatedtickets(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    caseref = models.IntegerField(db_column='caseRef') # Field name made lowercase.
    caserelated = models.IntegerField(db_column='caseRelated') # Field name made lowercase.
    class Meta:
        db_table = u'tRelatedTickets'

class Tclocks(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    cid = models.IntegerField(db_column='cID') # Field name made lowercase.
    clocktype = models.TextField(db_column='clockType') # Field name made lowercase.
    clockdate = models.TextField(db_column='clockDate', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'tClocks'

class Tpayroll(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    cutdate = models.TextField(db_column='CutDate') # Field name made lowercase. This field type is a guess.
    payrolldate = models.TextField(db_column='PayrollDate') # Field name made lowercase. This field type is a guess.
    pyarea = models.TextField(db_column='PYArea') # Field name made lowercase.
    reqtype = models.TextField(db_column='ReqType') # Field name made lowercase.
    endofpp = models.TextField(db_column='EndOfPP', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'tPayroll'

