CREATE LOGIN [nuggetlab\dvader]
FROM WINDOWS
GO

CREATE LOGIN [nuggetlab\DBAs]
FROM WINDOWS
GO

CREATE LOGIN JrDev
WITH PASSWORD = 'Str0ngP@55' MUST_CHANGE,  CHECK_EXPIRATION=ON, CHECK_POLICY=ON
GO

CREATE LOGIN SrDev
WITH PASSWORD = 'Str0ngP@55'
GO

USE NuggetlabDB
GO

--Normal Windows User
CREATE USER DBAs
FOR LOGIN [nuggetlab\DBAs]
GO

--Normal SQL User
CREATE USER JrDev
FOR LOGIN JrDev
GO
--Sproc User
CREATE USER SprocUser
WITHOUT LOGIN
GO
--Contained User
CREATE USER [nuggetlab\knox]

CREATE USER ContainedUser
WITH PASSWORD = 'Str0ngP@55'
GO
