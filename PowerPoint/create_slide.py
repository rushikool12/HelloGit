import collections.abc
from pptx import Presentation
pr1 = Presentation() #new presentaion 
slide1_register = pr1.slide_layouts[0] #add first slide 0 - title slide 
# 0 - title , 1 - title and content, 3 - section header 
slide2_register = pr1.slide_layouts[1]

slide1 = pr1.slides.add_slide(slide1_register)
slide2 = pr1.slides.add_slide(slide2_register)

#placeholder items in the layout 

title1 = slide1.shapes.title
subtitle1 = slide1.placeholders[1]

title2 = slide2.shapes.title 
bullet_point_box = slide2.shapes
bullet_point_level1 = bullet_point_box.placeholders[1]
bullet_point_level1.text = "First Bullet Point"
bullet_point_level2 = bullet_point_level1.text_frame.add_paragraph()
bullet_point_level2.text = "Sub level Second Bullet"
bullet_point_level2.level = 1 



#text in the slides 
title1.text = "FirstSlide"
subtitle1.text = "Just the first tutorial" 

title2.text = "Second Slide with Bullets" 

pr1.save("First_Presentation_2.pptx") #save presenatation 