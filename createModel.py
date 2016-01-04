#coding:utf-8

__author__ = 'Jerry'  
import sys

prefix = 'uro_'
  
""" 
title comment 
"""  
def fileTitleComment():  
    return """  /** 
    *author:Jerry 
    */\n"""  
  
  
""" 
help 
"""  
def showHelp():  
    print """help\n 
    example: 
 
    1:createObject.py obj:CWDemoObject 1 s:sName s:sTitle i:nID d:dBirtyday 
    2:createObject.py obj:CWDemoObject 0 s:sName s:sTitle i:nID d:dBirtyday 
    3:createObject.py obj:CWDemoObject s:sName s:sTitle i:nID d:dBirtyday 
    4:createObject.py CWDemoObject s:sName s:sTitle i:nID d:dBirtyday 
 
    obj:name (name means file name and object name.) 
    1: open arc flag ^-^ 
 
    s:NSString 
    i:NSInteger 
    d:NSDate"""  
  
""" 
@property (nonatomic, strong) NSString*     sCode; 
"""  
def writeObj(obj_string, fileHandle):  
    try:  
        (obj, name) = obj_string.strip().split(':')  
        if obj == 's':  
            fileHandle.write('@property (nonatomic, strong) NSString*\t\t\t%s;\n' %(name))  
        elif obj == 'i':  
            fileHandle.write('@property (nonatomic, assign) NSInteger\t\t\t%s;\n' %(name))  
        elif obj == 'd':  
            fileHandle.write('@property (nonatomic, strong) NSDate*\t\t\t%s;\n' %(name))  
  
    except ValueError as err:  
        print ('error %s' % (err))  
  
""" 
@synthesize _sCode; 
"""  
def writeSynthesize(obj_string, fileHandle):  
    try:  
        (obj, name) = obj_string.strip().split(':')  
        fileHandle.write('@synthesize _%s;\n' %(name))  
    except ValueError as err:  
        print ('error %s' % (err))  
  
  
""" 
    [object release]; 
"""  
def writeObjectRelease(obj_string, fileHandle):  
    try:  
        (obj, name) = obj_string.strip().split(':')  
        fileHandle.write('\n\t[_%s release];' % (name))  
    except ValueError as err:  
        print ('error %s' % (err))  
  
def createModel(*args):  
    # print args  
    try: 
        args  = args[0] 

        modelName = '@interface %s : PropertyObject' % args[1][4:]
        interfaceResult = ['#import "PropertyObject.h"', modelName, '']
        typeDict = {'int':'NSNumber', 
        'tinyint':'NSNumber', 
        'varchar':'NSString',
        'text':'NSString',
        'decimal':'NSDecimalNumber',
        'datetime':'NSString'}
        print args[1]
        #with open("%s.sql" % (args[1]), 'r') as fn:
        fn = open("%s.sql" % (args[1]), 'r')
        line = fn.readline()
        while line:
            #print line
            if line[0:3] == '  `':
                item = line.split(' ')
                print item[1][0:3]
                if item[3][0:3] == 'int' or item[3][0:7] == 'tinyint':
                    interfaceResult.append('@property (nonatomic, readonly) %s *%s;' % (typeDict['int'], str(item[2]).replace('`','')))
                elif item[3][0:7] == 'varchar' or item[3][0:4] == 'text':
                    interfaceResult.append('@property (nonatomic, readonly) %s *%s;' % (typeDict['varchar'], str(item[2]).replace('`','')))
                elif item[3][0:7] == 'decimal':
                    interfaceResult.append('@property (nonatomic, readonly %s *%s;' % (typeDict['decimal'], str(item[2]).replace('`','')))
                elif item[3][0:8] == 'datetime':
                    interfaceResult.append('@property (nonatomic, readonly %s *%s;' % (typeDict['datetime'], str(item[2]).replace('`','')))
            line = fn.next()
            print line
        #interfaceResult.append('')
        #interfaceResult.append('@end')
        #print interfaceResult
        #with open('%s.h' % modelName, 'w') as fileOutput:
        #    for item in interfaceResult:
        #        fileOutput.writelines(item)
        print 'over'

        """
        #create file.h  
        with open("%s.h" % (filename), 'w') as fn:  
            #write title comment  
            fn.write(fileTitleComment())  

            #write import file  

            fn.write('import <Foundation/Foundation.h>\n\n')  
            #write object  
            fn.write("@interface %s : NSObject\n\n" % (filename))  

            for eachObj in objs:  
                writeObj(eachObj, fn)  

            #write end  
            fn.write("\n@end")  

        #create file.m  
        with open("%s.m" % (filename), 'w') as fn:  
            #write import file  
            fn.write('#import "%s.h"\n\n' % (filename))  
            fn.write('@implementation %s\n\n' % (filename))  

            #@synthesize  
            for eachObj in objs:  
                writeSynthesize(eachObj, fn)  

            #init  
            fn.write('\n- (id) init {\n\tif (self = [super init]) {\n\t\t//add code\n\t}\n\treturn self;\n}')  

            #arc model  
            if bArc == False:  
                fn.write('\n\n- (void) dealloc {\n');  
                for eachObj in objs:  
                    writeObjectRelease(eachObj, fn)  
                fn.write('\n\n\t[super dealloc]\n}\n\n');  

            fn.write('\n@end')
        """
              
  
  
    except ValueError as err:
        print "error : %s" % (err)
        #print showHelp()  
  
if __name__ == '__main__':  
    createModel(sys.argv)  
