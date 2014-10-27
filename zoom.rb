########################################################################################
###  将指定目录（及子目录）下的所有高度超过 154 pixcels的图片按原来的宽高比缩放为高度为154 pixcels
###
###  前提条件：首先安装exifr及mini_magick模块
### => gem install exifr
### => brew install imagemagick
########################################################################################

require 'rubygems'
require 'exifr'
require 'find'
require 'FileUtils'
require 'mini_magick'

srcDir = "/Games/github/HelloPig/res/img"

def fileWalk(path)
	desDir = "/Games/github/HelloPig/res/img2"
  	Find.find(path) do |f|  
      type = "File" if File.file?(f)
      type  = "Dir " if File.directory?(f)
        if type != "File" && type != "Dir "
          type = "   ?"
        end
    #puts "#{type}: #{f}" 
    if type == "File" && f[/\.[^\.]+$/]==".jpg"
    	#puts f
    	mArray = f.split("/")
        folder = mArray[mArray.length - 2]
        fileName = mArray[mArray.length - 1]
        
        originalWidth = EXIFR::JPEG.new(f).width
        originalHeight = EXIFR::JPEG.new(f).height
        newWidth = 154.0 * (originalWidth * 1.0 / originalHeight)
        FileUtils.mkdir_p("#{desDir}/#{folder}")
        if originalHeight > 154
        	image = MiniMagick::Image.open(f)
			image.resize "#{newWidth}x154"
			image.write "#{desDir}/#{folder}/#{fileName}"
			puts "#{f}  " + "#{EXIFR::JPEG.new(f).width}" + "*" + "#{EXIFR::JPEG.new(f).height}" + "缩放完成！"
		else
			FileUtils.cp(f, "#{desDir}/#{folder}/#{fileName}")
			puts "#{f}  " + "#{EXIFR::JPEG.new(f).width}" + "*" + "#{EXIFR::JPEG.new(f).height}" + "直接拷贝！"
		end
		
   	end
  end 
end
 
fileWalk(srcDir) #put whatever folder here
