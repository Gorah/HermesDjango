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
    #tExternalErrors table to log errors in the tracker
    
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        )
    loggedby = models.SmallIntegerField(
        null=True,
        db_column='LoggedBy',
        blank=True
        )
    receivedon = models.DateTimeField(
        db_column='ReceivedOn',
        blank=True
        )
    errstatus = models.CharField(
        max_length=10,
        db_column='ErrStatus',
        blank=True
        )
    process = models.ForeignKey(
        Tprocess, null=True,
        db_column='Process',
        blank=True
        )
    issuedescr = models.TextField(
        db_column='IssueDescr',
        blank=True
        )
    employeeid = models.ForeignKey(
        Tmcbcemployee,
        null=True,
        db_column='EmployeeID',
        blank=True
        )
    errorbyparty = models.ForeignKey(
        Terrorparty,
        null=True,
        db_column='ErrorByParty',
        blank=True)
    errorbyperson = models.ForeignKey(
        Tmcbcemployee,
        null=True,
        db_column='ErrorByPerson',
        blank=True
        )
    resolution = models.TextField(
        db_column='Resolution',
        blank=True
        )
    affectedpayp = models.CharField(
        max_length=10,
        db_column='AffectedPayP',
        blank=True) 
    incorrectpay = models.BooleanField(
        null=True,
        db_column='IncorrectPay',
        blank=True
        )
    relatedcase = models.IntegerField(
        null=True,
        db_column='RelatedCase',
        blank=True) 
    impraction = models.TextField(
        db_column='ImprAction',
        blank=True
        ) 
    teamerr = models.CharField(
        max_length=10,
        db_column='TeamErr',
        blank=True
        )
    class Meta:
        db_table = u'tExternalErrors'
    

class Tpeerchecking(models.Model):
    #tPeerchecking table for storing peercheck notes. To be altered
    #with peerchecking module improvements
    
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        )
    relatedticket = models.IntegerField(
        null=True,
        db_column='relatedTicket',
        blank=True
        )
    auditor = models.IntegerField(
        null=True,
        db_column='Auditor',
        blank=True) 
    datechecked = models.DateTimeField(
        db_column='dateChecked',
        blank=True
        )
    dataentry = models.CharField(
        max_length=10,
        db_column='DataEntry',
        blank=True
        )
    processcorrect = models.CharField(
        max_length=10,
        db_column='ProcessCorrect',
        blank=True
        )
    sapcorrected = models.BooleanField(
        db_column='SAPCorrected'
        )
    processcorrected = models.BooleanField(
        db_column='ProcessCorrected'
        )
    completed = models.BooleanField(
        db_column='Completed'
        )
    comments = models.TextField(
        db_column='Comments',
        blank=True
        )
    class Meta:
        db_table = u'tPeerchecking'

class Tversion(models.Model):
    #tVersion table - storing current version number used to verify
    #if user is using correct version of the tool
    
    ver = models.CharField(
        max_length=5,
        primary_key=True,
        db_column='Ver'
        )
    class Meta:
        db_table = u'tVersion'

class Tmcbcemployee(models.Model):
    #tMCBCEmployee - contains all the details about clients employees
    
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        )
    forname = models.CharField(
        max_length=50,
        db_column='Forname',
        blank=True)
    surname = models.CharField(
        max_length=50,
        db_column='Surname',
        blank=True
        )
    payrollarea = models.CharField(
        max_length=5,
        db_column='PayrollArea',
        blank=True
        ) 
    eeid = models.IntegerField(
        null=True,
        db_column='EEID',
        blank=True
        )
    class Meta:
        db_table = u'tMCBCEmployee'

class Tsource(models.Model):
    #tSource - source of ticket options
    
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        ) 
    sourcename = models.CharField(
        max_length=15,
        db_column='SourceName',
        blank=True
        )
    class Meta:
        db_table = u'tSource'

class Tprocess(models.Model):
    #tProcess - table listing processes and their TAT types
    
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        )
    processname = models.CharField(
        max_length=70,
        db_column='ProcessName',
        blank=True
        )
    processtype = models.CharField(
        max_length=10,
        db_column='ProcessType',
        blank=True
        )
    letter = models.BooleanField(
        null=True,
        db_column='Letter',
        blank=True
        ) 
    class Meta:
        db_table = u'tProcess'

class Tcurrentstatus(models.Model):
    #tCurrentStatus - table containing statuses and their
    #clock behaviour
    
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        )
    currentstatus = models.CharField(
        max_length=50,
        db_column='CurrentStatus',
        blank=True
        )
    clockstop = models.BooleanField(
        db_column='ClockStop'
        )
    class Meta:
        db_table = u'tCurrentStatus'

class Tassignedto(models.Model):
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        )
    assignedto = models.CharField(
        max_length=50,
        db_column='AssignedTo',
        blank=True
        )
    active = models.BooleanField(
        db_column='Active'
        )
    class Meta:
        db_table = u'tAssignedTo'

class Tusrgroups(models.Model):
    #user groups available for users and for process grouping
    
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        )
    groupname = models.CharField(
        max_length=50,
        db_column='GroupName'
        )
    class Meta:
        db_table = u'tUsrGroups'

class Tusringroups(models.Model):
    #many-to-many table matching users to groups
    
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        )
    usrid = models.ForeignKey(
        Tuser,
        null=True,
        db_column='UsrID',
        blank=True)
    usrgroup = models.ForeignKey(
        Tusrgroups,
        null=True,
        db_column='usrGroup',
        blank=True
        )
    class Meta:
        db_table = u'tUsrInGroups'

class Tprocessassigment(models.Model):
    #many-to-many table matching processes to groups
    
    processid = models.ForeignKey(
        Tprocess,
        null=True,
        db_column='ProcessID',
        blank=True
        )
    groupid = models.ForeignKey(
        Tusrgroups,
        null=True,
        db_column='GroupID',
        blank=True
        )
    class Meta:
        db_table = u'tProcessAssigment'

class Tuser(models.Model):
    #tUser table storing all app users data
    
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        )
    username = models.CharField(
        max_length=60,
        db_column='UserName',
        blank=True
        )
    eeid = models.CharField(
        max_length=15,
        db_column='EeID',
        blank=True
        )
    passcode = models.CharField(
        max_length=15,
        db_column='PassCode',
        blank=True
        )
    userlvl = models.CharField(
        max_length=10,
        db_column='UserLvl',
        blank=True
        )
    active = models.BooleanField(
        null=True,
        db_column='Active',
        blank=True
        )
    class Meta:
        db_table = u'tUser'

class Terrorparty(models.Model):
    #tErrorParty - parties for errors table for FK in tExternalErrors
    
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        )
    partyname = models.CharField(
        max_length=70,
        db_column='PartyName',
        blank=True
        )
    class Meta:
        db_table = u'tErrorParty'

class Ttracker(models.Model):
    #tTracker - main table storing tickets that are added to DB.
    #Contains all the data about tickets and links with multiple FK's
    
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        )
    eeid = models.ForeignKey(
        Tmcbcemployee,
        null=True,
        db_column='EeID',
        blank=True
        )
    processid = models.ForeignKey(
        Tprocess,
        null=True,
        db_column='ProcessID',
        blank=True
        )
    casesubject = models.TextField(
        db_column='CaseSubject',
        blank=True
        )
    datereceived = models.DateTimeField(
        db_column='DateReceived',
        blank=True
        )
    sourceid = models.ForeignKey(
        Tsource,
        null=True,
        db_column='SourceID',
        blank=True
        )
    multipleemployees = models.BooleanField(
        db_column='MultipleEmployees'
        )
    multieenumber = models.SmallIntegerField(
        null=True,
        db_column='MultiEENumber',
        blank=True
        )
    pcrnumber = models.IntegerField(
        null=True,
        db_column='PCRNumber',
        blank=True)
    effectivedate = models.DateTimeField(
        db_column='EffectiveDate',
        blank=True
        )
    expedite = models.BooleanField(
        db_column='Expedite'
        )
    currentstatus = models.ForeignKey(
        Tcurrentstatus,
        null=True,
        db_column='CurrentStatus',
        blank=True
        )
    updatedate = models.DateTimeField(
        db_column='UpdateDate',
        blank=True
        )
    comments = models.TextField(
        db_column='Comments',
        blank=True
        )
    assignedto = models.ForeignKey(
        Tassignedto,
        null=True,
        db_column='AssignedTo',
        blank=True
        )
    closedate = models.DateTimeField(
        db_column='CloseDate',
        blank=True
        )
    timestart = models.DateTimeField(
        db_column='TimeStart',
        blank=True
        )
    timestop = models.DateTimeField(
        db_column='TimeStop',
        blank=True
        )
    tat = models.SmallIntegerField(
        null=True,
        db_column='TAT',
        blank=True
        )
    days_open = models.SmallIntegerField(
        null=True,
        db_column='Days_Open',
        blank=True
        ) 
    scanned = models.BooleanField(
        db_column='Scanned'
        )
    indexed = models.BooleanField(
        db_column='Indexed'
        )
    casedescription = models.TextField(
        db_column='CaseDescription',
        blank=True
        )
    requiredcompletiondate = models.DateTimeField(
        db_column='RequiredCompletionDate',
        blank=True
        )
    incorrectrequest = models.BooleanField(
        db_column='IncorrectRequest'
        )
    affectingpay = models.BooleanField(
        db_column='AffectingPay'
        )
    clockstop = models.BooleanField(
        db_column='ClockStop'
        )
    changelog = models.TextField(
        db_column='Changelog',
        blank=True
        )
    closedby = models.ForeignKey(
        Tuser,
        null=True,
        db_column='ClosedBy',
        blank=True
        )
    compareperiod = models.BooleanField(
        null=True,
        db_column='ComparePeriod',
        blank=True
        ) 
    inrejcomment = models.CharField(
        max_length=150,
        db_column='InRejComment',
        blank=True
        )
    lastupdate = models.DateTimeField(
        db_column='LastUpdate',
        blank=True
        )
    excludefromsla = models.BooleanField(
        null=True,
        db_column='ExcludeFromSLA',
        blank=True
        )
    relatedticket = models.TextField(
        db_column='RelatedTicket',
        blank=True
        )
    manualpcr = models.BooleanField(
        null=True,
        db_column='ManualPCR',
        blank=True
        )
    personassigned = models.ForeignKey(
        Tuser,
        null=True,
        db_column='PersonAssigned',
        blank=True
        )
    class Meta:
        db_table = u'tTracker'

class Sysdiagrams(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True
        )
    principal_id = models.IntegerField(
        unique=True
        )
    diagram_id = models.AutoField(
        primary_key=True
        )
    version = models.IntegerField(
        null=True,
        blank=True
        )
    definition = models.TextField(
        blank=True
        )
    class Meta:
        db_table = u'sysdiagrams'

class Tchecklistsource(models.Model):
    #TBD if used 
    
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        )
    formname = models.CharField(
        max_length=50,
        db_column='FormName'
        )
    sourcetablename = models.CharField(
        max_length=50,
        db_column='SourceTableName'
        )
    class Meta:
        db_table = u'tChecklistSource'

class Tchecklistassigment(models.Model):
    #TBD if used
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        )
    processid = models.ForeignKey(
        Tprocess,
        null=True,
        db_column='ProcessID',
        blank=True
        )
    formid = models.ForeignKey(
        Tchecklistsource,
        null=True,
        db_column='FormID',
        blank=True
        )
    class Meta:
        db_table = u'tChecklistAssigment'

class Trelatedtickets(models.Model):
    #Table to store relation pairs between tickets.
    #Each entry in related ticket field generates 2 rows in this table
    #first row puts origin case as caseref, and related case in caserelated
    #second row is the other way around, to allow displaying origin case
    #as related to second one in display of the latter.
    
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        )
    caseref = models.IntegerField(
        db_column='caseRef'
        )
    caserelated = models.IntegerField(
        db_column='caseRelated'
        )
    class Meta:
        db_table = u'tRelatedTickets'

class Tclocks(models.Model):
    """Table to store clock activity for each ticket. This means each
    clock start (ie: opening the ticket) or clock stop (ie: closing
    the ticket or putting it on pending with client action) will get
    registered here. Those entries are then used to calculate TAT
    """
    
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        )
    cid = models.IntegerField(
        db_column='cID'
        )
    clocktype = models.CharField(
        max_length=5,
        db_column='clockType'
        )
    clockdate = models.DateTimeField(
        db_column='clockDate',
        blank=True
        )
    class Meta:
        db_table = u'tClocks'

class Tpayroll(models.Model):
    '''
    Table to store payroll run related details like cutoff date,
    payroll date, type of payroll, payperiod end. All those details
    are used when calculating Required Completion Date for PY TAT
    tickets.
    '''
    id = models.AutoField(
        primary_key=True,
        db_column='ID'
        )
    cutdate = models.DateTimeField(
        db_column='CutDate'
        )
    payrolldate = models.DateTimeField(
        db_column='PayrollDate'
        )
    pyarea = models.CharField(
        max_length=5,
        db_column='PYArea'
        )
    reqtype = models.CharField(
        max_length=5,
        db_column='ReqType'
        ) 
    endofpp = models.DateTimeField(
        db_column='EndOfPP',
        blank=True) 
    class Meta:
        db_table = u'tPayroll'

class Vw_Tracker_View_All(models.Model):
    '''
    DB view to show unfiltered tracker display of tickets
    '''

    id = models.IntegerField(
        null=True,
        db_column='ID'
        )
    processname = models.CharField(
        max_length=70,
        null = True,
        db_column='ProcessName')
    datereceived = models.DateTimeField(
        null=True,
        db_column='DateReceived'
        )
    tat = models.SmallIntegerField(
        null = True,
        db_column='TAT'
        )
    days_open = models.SmallIntegerField(
        null=True,
        db_column='Days_Open'
        )
    pcrnumber = models.IntegerField(
        null=True,
        db_column='PCRNumber'
        )
    expedite = models.BooleanField(
        null=True,
        db_column='Expedite'
        )
    assignedto = models.CharField(
        max_length=50,
        null=True,
        db_column='AssignedTo'
        )
    username = models.CharField(
        max_length=60,
        null=True,
        db_column='UserName'
        )
    currentstatus = models.CharField(
        max_length=50,
        null=True,
        db_column='CurrentStatus'
        )
    closedate = models.DateTimeField(
        null=True,
        db_column='CloseDate'
        )
    requiredcompletiondate = models.DateTimeField(
        null=True,
        db_column='ReqiredCompletionDate'
        )
    sourcename = models.CharField(
        max_length=15,
        null=True,
        db_column='SourceName'
        )
    surname = models.CharField(
        max_length=50,
        null=True,
        db_column='Surname'
        )
    forname = models.CharField(
        max_length=50,
        null=True,
        db_column='Forname'
        )
    effectivedate = models.DateTimeField(
        null=True,
        db_column='EffectiveDate'
        )
    eeid = models.IntegerField(
        null=True,
        db_column='EEID'
        )
    processtype = models.CharField(
        max_length=10,
        null=True,
        db_column='ProcessType'
        )
    lastupdate = models.DateTimeField(
        null=True,
        db_column='LastUpdate'
        )
    peerid = models.IntegerField(
        null=True,
        db_column='PeerID'
        )
    class Meta:
        db_table=u'vw_Tracker_view_All'
        managed = False
    
