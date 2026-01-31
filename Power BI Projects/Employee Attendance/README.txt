1] Defined a variable folder_path to store the directory location of the report files.
	folder_path = path of the folder

2] Utilized the folder_path variable to dynamically refer and load the source files:

	Attendance_Data = folder_path & "\Attendance Data.xlsx"
	Employee_Details = folder_path & "\Employee Details.xlsx"

3] Attendance_Table
	Combined the files in a folder. [Attendance data files].

4] Date_Table
	Created a centralized Date Table to serve as a common dimension table, establishing relationships with all fact tables containing date fields. This enables the use of Date_Table[Date] in slicers for dynamic and consistent date filtering across the entire data model.

5] Attendance_Data
	In the Attendance_Data table, calculated key duration metrics (Break Duration, Working Duration, and Total Duration) using DAX functions.

6] Attendance_Report
	Developed an Attendance_Report summary table that aggregates Break Hours, Working Hours, and Total Hours, summarized by Employee ID and Log DateTime using DAX measures.