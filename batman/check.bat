@echo off
@chcp 866

cd %systemroot%

REM загруженность CPU
for /f %%a in ('wmic cpu get LoadPercentage /value^|find "="' ) do set "%%a">C:\check_list\used_cpu.txt
echo %LoadPercentage%>C:\check_list\used_cpu.txt

REM общее количество RAM
for /f %%и in ('wmic os get TotalVisibleMemorySize /value^|find "="' ) do set "%%и">C:\check_list\total_ram.txt
echo %TotalVisibleMemorySize%>C:\check_list\total_ram.txt

REM количество свободной RAM
for /f %%с in ('wmic os get FreePhysicalMemory /value^|find "="' ) do set "%%с">C:\check_list\free_ram.txt
echo %FreePhysicalMemory%>C:\check_list\free_ram.txt

REM вычисление загруженности RAM
FOR /F %%x IN (C:\check_list\total_ram.txt) DO (
set /a t=%%x
)
FOR /F %%y IN (C:\check_list\free_ram.txt) DO (
set /a f=%%y
)
set /a z= t - f
echo %z%>C:\check_list\used_ram.txt

REM Информация по HDD
setlocal enableextensions enabledelayedexpansion
for /f "skip=1 tokens=1-3" %%i in ('2^>nul ^
WMIC LogicalDisk ^
WHERE "DriveType='3'" ^
GET FreeSpace^, Name^, Size^') do (
set sFreeSize=%%i
set sFreeSizeOf=%%k
if NOT 1%%j==1 (
set /A Free=1
set /A Size=!sFreeSizeOf:~0,-3!/1024/1024
set /A prc=!Size!/100*3
set /A Size=!Size!-!prc!
set /A Free=!sFreeSize:~0,-3!/1024/1024
set /A prcc=!Free!/100*3
set /A Free=!Free!-!prcc!
set /A Procent=!Free!*100/!Size!
set /A a+=!Size!
set /A al+=!free!
set /A all+=!Procent!
set /A z=!Size!-!Free!
echo !z!>C:\check_list\hdd_used_%%j
echo !Size!>C:\check_list\hdd_total_%%j
rem ren "C:\check_list\*.*" *.txt
))

exit