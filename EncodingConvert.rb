########################################################################################
###  将指定目录（及子目录）下的所有后缀为.lrc的文件内容字符编码统一转换为utf-8
###
###  前提条件：首先安装charlock_holmes模块
### => gem install charlock_holmes -- --with-icu-dir=/path/to/installed/icu4c
########################################################################################

require "iconv"
#require "nkf" 
require 'charlock_holmes'
require 'rubygems'
require 'find'
require 'FileUtils' 



def fileWalk()
	srcDir = "~/newTemp/mp3"
  	Find.find(srcDir) do |f|  
    	type = "File" if File.file?(f)
      	type  = "Dir " if File.directory?(f)
        if type != "File" && type != "Dir "
          type = "   ?"
        end
	    #puts "#{type}: #{f}" 
	    if type == "File" && f[/\.[^\.]+$/]==".lrc"
	    	#puts f
	    	mArray = f.split("/")
	        folder = mArray[mArray.length - 2]
	        fileName = mArray[mArray.length - 1]
	        #puts fileName

	       	content = File.read("#{srcDir}/#{fileName}") 
			detection = CharlockHolmes::EncodingDetector.detect(content)
			utf8_encoded_content = CharlockHolmes::Converter.convert content, detection[:encoding], 'UTF-8'

			file = File.new("#{srcDir}/#{fileName}","w+")
			file.puts(utf8_encoded_content)
			puts "#{fileName} 处理完毕！"	
			
	   	end
  end 
end
 
fileWalk() #put whatever folder here
