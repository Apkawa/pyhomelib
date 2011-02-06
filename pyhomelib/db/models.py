from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Info(Base):
    '''
        CREATE TABLE IF NOT EXISTS info
                                        (name varchar(32),
                                         value varchar(255),
                                         PRIMARY KEY (name));
    '''
    __tablename__ = 'info'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    value = Column(String(255))

class Book(Base):
    '''
        CREATE TABLE IF NOT EXISTS libbook
                                        (bookid integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                                         title varchar(255),
                                         lang char(2),
                                         year smallint,
                                         authorid integer,
                                         genreid integer,
                                         seqid integer,
                                         fileauthor varchar(64),
                                         filetype char(4) NOT NULL DEFAULT '',
                                         filesize int,
                                         md5 char(32) NOT NULL,
                                         UNIQUE (md5));
    '''
    __tablename__ = 'libbook'

class Author(Base):
    '''
        CREATE TABLE IF NOT EXISTS libauthor
                                        (bookid integer,
                                         authorid integer,
                                         PRIMARY KEY (bookid, authorid));
    '''


class AuthorName(Base):
    '''
        CREATE TABLE IF NOT EXISTS libauthorname
                                        (authorid integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                                         firstname varchar(99) NOT NULL DEFAULT '',
                                         middlename varchar(99) NOT NULL DEFAULT '',
                                         lastname varchar(99) NOT NULL DEFAULT '',
                                         nickname varchar(33) NOT NULL DEFAULT '');
    '''
    pass

class Sequence(Base):
    '''
        CREATE TABLE IF NOT EXISTS libsequence
                                        (bookid integer,
                                         seqid integer,
                                         seqnum int,
                                         PRIMARY KEY (bookid, seqid));
    '''

class Seqname(Base):
    '''
        CREATE TABLE IF NOT EXISTS libseqname
                                        (seqid integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                                         seqname varchar(255),
                                         UNIQUE (seqname));
    '''


class Genre(Base):
    '''
        CREATE TABLE IF NOT EXISTS libgenre
                                        (bookid integer,
                                         genreid integer,
                                         PRIMARY KEY (bookid, genreid));
    '''
class GenreList(Base):
    '''
        CREATE TABLE IF NOT EXISTS libgenrelist
                                        (genreid integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                                         genrecode varchar(45),
                                         genredesc varchar(99),
                                         UNIQUE(genrecode));
    '''

class FileName(Base):
    '''
        CREATE TABLE IF NOT EXISTS libfilename
                                        (bookid integer,
                                         filename varchar(32767),
                                         PRIMARY KEY(bookid),
                                         UNIQUE(filename));
    '''
class Group(Base):
    '''
        CREATE TABLE IF NOT EXISTS libgroup
                                        (bookid integer,
                                         groupid integer,
                                         PRIMARY KEY (bookid, groupid));
    '''

class GroupList(Base):
    '''
        CREATE TABLE IF NOT EXISTS libgrouplist
                                        (groupid integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                                         groupname varchar(32),
                                         UNIQUE(groupname));
    '''
'''



        CREATE INDEX IF NOT EXISTS idx_libbook_title ON libbook(title);
        CREATE INDEX IF NOT EXISTS idx_libbook_lang ON libbook(lang);
        CREATE INDEX IF NOT EXISTS idx_libbook_authorid ON libbook(authorid);
        CREATE INDEX IF NOT EXISTS idx_libbook_genreid ON libbook(genreid);
        CREATE INDEX IF NOT EXISTS idx_libbook_seqid ON libbook(seqid);
        CREATE INDEX IF NOT EXISTS idx_libbook_fileauthor ON libbook(fileauthor);
        CREATE UNIQUE INDEX IF NOT EXISTS idx_libbook_md5 ON libbook(md5);

        CREATE INDEX IF NOT EXISTS idx_libauthor_bookid ON libauthor(bookid);
        CREATE INDEX IF NOT EXISTS idx_libauthor_authorid ON libauthor(authorid);

        CREATE INDEX IF NOT EXISTS idx_libauthorname_firstname ON libauthorname(firstname);
        CREATE INDEX IF NOT EXISTS idx_libauthorname_middlename ON libauthorname(middlename);
        CREATE INDEX IF NOT EXISTS idx_libauthorname_lastname ON libauthorname(lastname);
        CREATE INDEX IF NOT EXISTS idx_libauthorname_nickname ON libauthorname(nickname);

        CREATE INDEX IF NOT EXISTS idx_libsequence_bookid ON libsequence(bookid);
        CREATE INDEX IF NOT EXISTS idx_libsequence_seqid ON libsequence(seqid);

        CREATE UNIQUE INDEX IF NOT EXISTS idx_libseqname_seqname ON libseqname(seqname);

        CREATE INDEX IF NOT EXISTS idx_libgenre_bookid ON libgenre(bookid);
        CREATE INDEX IF NOT EXISTS idx_libgenre_genreid ON libgenre(genreid);

        CREATE UNIQUE INDEX IF NOT EXISTS idx_libfilename_filename ON libfilename(filename);

        CREATE INDEX IF NOT EXISTS idx_libgroup_bookid ON libgroup(bookid);
        CREATE INDEX IF NOT EXISTS idx_libgroup_groupid ON libgroup(groupid)
'''
