CREATE TABLE PerInfo(
    IDcardNo TEXT NOT NULL PRIMARY KEY,
    perName TEXT NOT NULL,
    address TEXT,
    height  INTEGER,
    eMail   TEXT,
    birthDay TEXT,
    birthPlace TEXT,
    isMarry INTEGER,
    education INTEGER,
    school TEXT,
    sex INTEGER,
    qq INTEGER,
    phoneNo INTEGER NOT NULL,
    wx TEXT,
    politicalStatus INTEGER,
    hukou TEXT,
    work  TEXT,
    createTime INTEGER,
    updateTime INTEGER,
    power INTEGER,
    enable INTEGER,
    introduce TEXT,
    temp1 TEXT,
    temp2 TEXT,
    temp3 TEXT,
    temp4 TEXT,
    temp5 TEXT
)
    
CREATE TABLE Works(
    work TEXT NOT NULL,
    createtime INTEGER
)

CREATE TABLE askforwork(
    createtime INTEGER NOT NULL,
    worktime INTEGER NOT NULL,
    IDcardNo INTEGER NOT NULL
)

CREATE TABLE work(
    createtime INTEGER NOT NULL,
    workname TEXT,
    worknum INTEGER,
    company TEXT,
    picture TEXT,
    aboutcompany TEXT,
    aboutwork TEXT,
    salary TEXT,
    workaddress TEXT,
    endtime TEXT,
    status INTEGER,
    temp1 TEXT,
    temp2 TEXT,
    temp3 TEXT,
    temp4 TEXT,
    temp5 TEXT    
)

delete from works where work = ''

delete from perinfo

delete from work where workname=''