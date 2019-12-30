<html xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
<meta name=ProgId content=Word.Document>
<meta name=Generator content="Microsoft Word 15">
<meta name=Originator content="Microsoft Word 15">
<link rel=File-List
href="Create%20Core%20Standard%20Feature%20Class%20in%20an%20Existing%20File%20Geodatabase_files/filelist.xml">
<link rel=Preview
href="Create%20Core%20Standard%20Feature%20Class%20in%20an%20Existing%20File%20Geodatabase_files/preview.wmf">

</head>

<body lang=EN-US style='tab-interval:.5in'>

<div class=WordSection1>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoListParagraphCxSpFirst><b style='mso-bidi-font-weight:normal'><span
style='font-size:14.0pt;mso-bidi-font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>These tools and scripts are provided
for educational use only. These were written by what is unarguably the worst
Python coder in the world, but they get the job done. What is the job?
Automating repetitive data management and creation tasks and ensuring that
consistent schema and data standards are applied across all databases. Find
something wrong (actually can you find the 458 errors?)? Log an “Issue” and
maybe I’ll fix it. Got a better idea? Spoon the repo and perhaps I’ll merge it
back into the source. <o:p></o:p></span></b></p>

<p class=MsoListParagraphCxSpMiddle><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p>&nbsp;</o:p></span></p>

<p class=MsoListParagraphCxSpMiddle><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p>&nbsp;</o:p></span></p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-.25in;mso-list:l0 level1 lfo1'><![if !supportLists]><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'><span style='mso-list:Ignore'>1.<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></span><![endif]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>Create Core
Standard Feature Class in an Existing File Geodatabase:</span></b><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'> </span><span lang=EN style='font-size:12.0pt;
line-height:107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin;
color:#4C4C4C;mso-ansi-language:EN'>Use this tool when a NPS core standard
feature class is required in an existing geodatabase. Execute the tool with
user-supplied parameters. The recommend output location is the default
geodatabase created when a new Pro project is created if the user has opted for
that to occur in Project Options. Many parameters can be set as defaults in the
tool properties. This will create all of the fields specified in the standard,
as well as set default domain (pick list) values, and set certain fields as
&quot;required&quot; (can't delete the field). This tool can be run multiple
times against the same geodatabase, for example, to create a point, polygon,
and polyline feature class all using the same schema. Additional executions of
the tool will detect the presence of existing required domains and will not
overwrite them. This tool cannot be executed against an existing feature class
and will return an error if attempted.</span><span style='font-size:12.0pt;
line-height:107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p></o:p></span></p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-.25in;mso-list:l0 level1 lfo1'><![if !supportLists]><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'><span style='mso-list:Ignore'>2.<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></span><![endif]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>Create
Standard GDB in Choice of Location:</span></b><span style='font-size:12.0pt;
line-height:107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>
Use this tool when a NPS core standard feature class is required in a new
geodatabase located in a path\folder that is determined by the user. Execute
the tool with user-supplied parameters. The recommend output location of the
File Geodatabase is in the &quot;Root&quot; of the Pro project folder. Many
parameters can be set as defaults in the tool properties. This will create all
of the fields specified in the standard, as well as set default domain (pick
list) values, and set certain fields as &quot;required&quot; (can't delete the
field).<o:p></o:p></span></p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-.25in;mso-list:l0 level1 lfo1'><![if !supportLists]><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'><span style='mso-list:Ignore'>3.<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></span><![endif]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>Create
Standard GDB in Enforced Location in Pro Project: </span></b><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>Use this tool when a NPS core standard feature
class is required in a new geodatabase located in a path\folder that is
specified in a data management SOP. Execute the tool with user-supplied
parameters after executing Create Folders in Pro Project. This will place the
File Geodatabase in a subfolder within the Pro project folder where the
subfolder is the required location of project <span class=SpellE>geodata</span>
regardless of how &quot;Pro is intended to be used&quot;. Many parameters can
be set as defaults in the tool properties. This will create all of the fields
specified in the standard, as well as set default domain (pick list) values,
and set certain fields as &quot;required&quot; (can't delete the field).
Changing the output location of the geodatabase requires modification of the
python source, explained elsewhere in this document.<o:p></o:p></span></p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-.25in;mso-list:l0 level1 lfo1'><![if !supportLists]><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'><span style='mso-list:Ignore'>4.<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></span><![endif]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>Create
Folders In Pro Project:</span></b><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'> Used for
new work, once a new Pro Project has been created, run this tool to create the
&quot;standard&quot; project folder directory within the project. Can be used
for existing work: with caution, most existing project folders are not
compatible with how <span class=GramE>Pro</span> &quot;manages&quot; project folders
and files. This tool satisfies any data management plan requirements that <span
class=SpellE>geodata</span> reside in a specified location and only in that
location.<o:p></o:p></span></p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-.25in;mso-list:l0 level1 lfo1'><![if !supportLists]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><span
style='mso-list:Ignore'>5.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span></b><![endif]><b style='mso-bidi-font-weight:normal'><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>Add Extended Core Attributes to Existing
Feature Class: </span></b><span lang=EN style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin;color:#4C4C4C;
mso-ansi-language:EN'>This tool is used when the user has an existing
geodatabase feature class that requires the NPS Core Extended attributes and
domains. Execute the tool with user-supplied parameters after executing the
Create Core Standard Feature Class tool in an Existing File Geodatabase, Create
Standard GDB in Enforced Location in Pro Project, Create Standard GDB in Choice
of Location, on a feature class created by another process, or a pre-existing
feature class. This will create all of the extended fields specified in the
standard, as well as set default domain (pick list) values. Only those fields
that are checked in the tool dialogue and affiliated domains will be created. This
tool can also be run multiple times against the same feature class, for
example, if the first tool execution only added one field, subsequent tool executions
against the same feature class can add additional fields. Tool validation will
detect the presence of existing extended fields and domains and will not
overwrite them if they exist.</span><b style='mso-bidi-font-weight:normal'><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'><o:p></o:p></span></b></p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-.25in;mso-list:l0 level1 lfo1'><![if !supportLists]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><span
style='mso-list:Ignore'>6.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span></b><![endif]><b style='mso-bidi-font-weight:normal'><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>Add GRSM Core Attributes to Existing Feature
Class: </span></b><span lang=EN style='font-size:12.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin;color:#4C4C4C;
mso-ansi-language:EN'>This tool is used when the user has an existing
geodatabase feature class that requires the GRSM Core attributes and domains.
Execute the tool with user-supplied parameters after executing the Create Core
Standard Feature Class tool in an Existing File Geodatabase, Create Standard
GDB in Enforced Location in Pro Project, Create Standard GDB in Choice of
Location, on a feature class created by another process, or a pre-existing
feature class. This will create all of the extended fields specified in the
standard, as well as set default domain (pick list) values. The GRSM version of
this tool presents the user with some choice of fields at run time (check
boxes) however not requiring any of the optional fields is not a reason to not
execute this tool: this tool adds required GRSM fields and domains to a feature
class even if no optional fields are chosen in the tool dialogue, and must be
executed against any GRSM feature class not containing the required fields (<span
class=SpellE>e.g</span> VALID). This tool also makes some changes to the
required NPS core schema: changes the default value of some attributes to
another value from the NPS core schema other than the default value specified
by the standard and adds a domain for MAPMETHOD. This tool can also be run
multiple times against the same feature class, for example, if the first tool
execution only added one field, subsequent tool executions against the same
feature class can add additional fields. Tool validation will detect the
presence of existing GRSM fields and domains and will not overwrite them if
they exist.</span><b style='mso-bidi-font-weight:normal'><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'><o:p></o:p></span></b></p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-.25in;mso-list:l0 level1 lfo1'><![if !supportLists]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><span
style='mso-list:Ignore'>7.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span></b><![endif]><b style='mso-bidi-font-weight:normal'><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>Add GRSM Fisheries Core Attributes to Existing
Feature Class:<span style='mso-spacerun:yes'>  </span></span></b><span lang=EN
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin;color:#4C4C4C;mso-ansi-language:EN'>This tool
is used when the user has an existing geodatabase feature class that requires
the GRSM Core attributes and domains. Execute the tool with user-supplied
parameters after executing the Create Core Standard Feature Class tool in an
Existing File Geodatabase, Create Standard GDB in Enforced Location in Pro
Project, Create Standard GDB in Choice of Location, on a feature class created
by another process, or a pre-existing feature class. This will create all of
the extended fields specified in the standard, as well as set default domain
(pick list) values. The GRSM version of this tool presents the user with some
choice of fields at run time (check boxes) however not requiring any of the
optional fields is not a reason to not execute this tool: this tool adds
required GRSM fields and domains to a feature class even if no optional fields
are chosen in the tool dialogue, and must be executed against any GRSM feature
class not containing the required fields (<span class=SpellE>e.g</span> VALID).
This tool also makes some changes to the required NPS core schema: changes the
default value of some attributes to another value from the NPS core schema
other than the default value specified by the standard and adds a domain for
MAPMETHOD. This tool can also be run multiple times against the same feature
class, for example, if the first tool execution only added one field,
subsequent tool executions against the same feature class can add additional
fields. Tool validation will detect the presence of existing GRSM fields and
domains and will not overwrite them if they exist.</span><b style='mso-bidi-font-weight:
normal'><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'><o:p></o:p></span></b></p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-.25in;mso-list:l0 level1 lfo1'><![if !supportLists]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><span
style='mso-list:Ignore'>8.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span></b><![endif]><b style='mso-bidi-font-weight:normal'><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>Add Standard Core Attributes to Existing Empty
Feature Class: </span></b><span lang=EN style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin;color:#4C4C4C;
mso-ansi-language:EN'>Use this tool when a NPS core standard is required in an
existing feature class that has no data. Execute the tool with user-supplied
parameters. Many parameters can be set as defaults in the tool properties. This
will create all of the fields specified in the standard, as well as set default
domain (pick list) values, and set certain fields as &quot;required&quot;
(can't delete the field). This tool can be run multiple times against the same
geodatabase, for example, to create a point, polygon, and polyline feature
class all using the same schema. Additional executions of the tool will detect
the presence of existing required domains and will not overwrite them.</span><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p></o:p></span></b></p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-.25in;mso-list:l0 level1 lfo1'><![if !supportLists]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><span
style='mso-list:Ignore'>9.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span></b><![endif]><b style='mso-bidi-font-weight:normal'><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>Add Standard Core Attributes to Existing
Non-Empty Feature Class: </span></b><span lang=EN style='font-size:12.0pt;
line-height:107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin;
color:#4C4C4C;mso-ansi-language:EN'>Use this tool when a NPS core standard is
required in an existing feature class that is populated with data. Execute the
tool with user-supplied parameters. Many parameters can be set as defaults in
the tool properties. This will create all of the fields specified in the
standard, as well as set default domain (pick list) values, and set certain
fields as &quot;required&quot; (can't delete the field). This tool can be run
multiple times against the same geodatabase, for example, to create a point,
polygon, and polyline feature class all using the same schema. Additional
executions of the tool will detect the presence of existing required domains
and will not overwrite them.</span><b style='mso-bidi-font-weight:normal'><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'><o:p></o:p></span></b></p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-.25in;mso-list:l0 level1 lfo1'><![if !supportLists]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><span
style='mso-list:Ignore'>10.<span style='font:7.0pt "Times New Roman"'>&nbsp; </span></span></span></b><![endif]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>Calculate
Coordinates: </span></b><span style='font-size:12.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>This tool is used
to update X_COORD, Y_COORD, LON, and LAT Fields with current coordinates when a
new feature is added or an existing one moved.<b style='mso-bidi-font-weight:
normal'><o:p></o:p></b></span></p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-.25in;mso-list:l0 level1 lfo1'><![if !supportLists]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><span
style='mso-list:Ignore'>11.<span style='font:7.0pt "Times New Roman"'>&nbsp; </span></span></span></b><![endif]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>Calculate
Elevation: </span></b><span style='font-size:12.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>This tool is used
to attribute elevation for new or modified features.<b style='mso-bidi-font-weight:
normal'><o:p></o:p></b></span></p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-.25in;mso-list:l0 level1 lfo1'><![if !supportLists]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><span
style='mso-list:Ignore'>12.<span style='font:7.0pt "Times New Roman"'>&nbsp; </span></span></span></b><![endif]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>Update
Administrative Boundaries for Features: </span></b><span style='font-size:12.0pt;
line-height:107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>This
tool is used to attribute &quot;Administrative Boundaries&quot; to a feature
class. Administrative boundaries delineate data into reportable administrative
classes.<b style='mso-bidi-font-weight:normal'><o:p></o:p></b></span></p>

<p class=MsoListParagraphCxSpLast style='text-indent:-.25in;mso-list:l0 level1 lfo1'><![if !supportLists]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><span
style='mso-list:Ignore'>13.<span style='font:7.0pt "Times New Roman"'>&nbsp; </span></span></span></b><![endif]><b
style='mso-bidi-font-weight:normal'><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>Update Name
of Nearest Line Feature for Features: </span></b><span style='font-size:12.0pt;
line-height:107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>This
tool is used to attribute nearest line features to a point feature class.
Nearest line features such as road and trail provide context to the location of
a feature.<b style='mso-bidi-font-weight:normal'><o:p></o:p></b></span></p>

</div>

</body>

</html>
