import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image ,ImageTk
import customtkinter as ctk
# from tkinter.messagebox import showerror


# Defining Main theme of all widgets
ctk.set_appearance_mode( "dark" )
ctk.set_default_color_theme( "dark-blue" )
wid = 1200
hgt = 700

def Imgo( file, w, h) :

    # Image processing
    img = Image.open( file )
    pht = ImageTk.PhotoImage( img.resize( (w,h), Image.ANTIALIAS))
    return pht

def change( can, page) :

    # Switching canvas
    can.destroy()
    page()

def clearBack() :

     # Defining Structure
    third_page = Canvas( root, width = wid, height = hgt, bg = "black", highlightcolor = "#3c5390", borderwidth = 0 )
    third_page.pack( fill = "both", expand = True )

    # Background Image
    back_image = Imgo( r'Backgroud\Clear_Back_Page.jpg', 1498, 875)
    third_page.create_image( 0, 0, image = back_image , anchor = "nw")

    # Heading
    third_page.create_text( 500, 120, text = "Remove Background", font = ( ft[0], 45, "bold"), fill = "#1c54df" )

    # Return Button
    ret = Imgo( r'Design\arrow.png', 45, 35)
    ret_bt = ctk.CTkButton( master = root, image = ret, text = None, width = 60, height = 40, corner_radius = 23,
                         bg_color = "#d3eafc", fg_color = "red", hover_color = "#ff5359", border_width = 0,
                         command = lambda : change( third_page, menuPage) )
    ret_bt_win = third_page.create_window( 30, 20, anchor = "nw", window = ret_bt )

    root.mainloop()

def convertImage() :

     # Defining Structure
    fourth_page = Canvas( root, width = wid, height = hgt, bg = "black", highlightcolor = "#3c5390", borderwidth = 0 )
    fourth_page.pack( fill = "both", expand = True )

    # Background Image
    back_image = Imgo( r'Backgroud\Convert_Img_Page.jpg', 1498, 875)
    fourth_page.create_image( 0, 0, image = back_image , anchor = "nw")

    # Heading
    fourth_page.create_text( 500, 120, text = "Convert Images", font = ( ft[0], 45, "bold" ), fill = "#1c54df" )

    # Return Button
    ret = Imgo( r'Design\arrow.png', 45, 35)
    ret_bt = ctk.CTkButton( master = root, image = ret, text = None, width = 60, height = 40, corner_radius = 23,
                         bg_color = "#d3eafc", fg_color = "red", hover_color = "#ff5359", border_width = 0,
                         command = lambda : change( fourth_page, menuPage) )
    ret_bt_win = fourth_page.create_window( 30, 20, anchor = "nw", window = ret_bt )

    root.mainloop()

def findImage() :

     # Defining Structure
    fifth_page = Canvas( root, width = wid, height = hgt, bg = "black", highlightcolor = "#3c5390", borderwidth = 0 )
    fifth_page.pack( fill = "both", expand = True )

    # Background Image
    back_image = Imgo( r'Backgroud\Find_Img_Page.jpg', 1498, 875)
    fifth_page.create_image( 0, 0, image = back_image , anchor = "nw")

    # Heading
    fifth_page.create_text( 400, 120, text = "Find Image", font = ( ft[0], 45, "bold" ), fill = "#1c54df" )

    # Return Button
    ret = Imgo( r'Design\arrow.png', 45, 35 )
    ret_bt = ctk.CTkButton( master = root, image = ret, text = None, width = 60, height = 40, corner_radius = 23,
                         bg_color = "#d3eafc", fg_color = "red", hover_color = "#ff5359", border_width = 0, 
                         command = lambda : change( fifth_page, menuPage) )
    ret_bt_win = fifth_page.create_window( 30, 20, anchor = "nw", window = ret_bt )

    root.mainloop()

def sortImage() :

     # Defining Structure
    sixth_page = Canvas( root, width = wid, height = hgt, bg = "black", highlightcolor = "#3c5390", borderwidth = 0 )
    sixth_page.pack( fill = "both", expand = True )

    # Background Image
    back_image = Imgo( r'Backgroud\Sort_Image_Page.jpg', 1498, 875)
    sixth_page.create_image( 0, 0, image = back_image , anchor = "nw")

    # Heading
    sixth_page.create_text( 400, 120, text = "Sort Images", font = ( ft[0], 45, "bold" ), fill = "#1c54df" )

    # Return Button
    ret = Imgo( r'Design\arrow.png', 45, 35)
    ret_bt = ctk.CTkButton( master = root, image = ret, text = None, width = 60, height = 40, corner_radius = 23,
                         bg_color = "#d3eafc", fg_color = "red", hover_color = "#ff5359", border_width = 0, 
                         command = lambda : change( sixth_page, menuPage) )
    ret_bt_win = sixth_page.create_window( 30, 20, anchor = "nw", window = ret_bt )

    root.mainloop()

def menuPage() :

    # Defining Structure
    second_page = Canvas( root, width = wid, height = hgt, bg = "black", highlightcolor = "#3c5390", borderwidth = 0 )
    second_page.pack( fill = "both", expand = True )

    # Background Image
    back_image = Imgo( r'Backgroud\Menu_Page.jpg', 1498, 875)
    second_page.create_image( 0, 0, image = back_image , anchor = "nw")

    # Heading
    second_page.create_text( 350, 120, text = "Content...", font = ( ft[0], 45, "bold" ), fill = "#1c54df" )

    # Back Ground remover page window
    backRem = Imgo( r'Design\Clear_Back_logo.png', 220, 200 )
    backRem_bt = ctk.CTkButton( master = root, image = backRem, text = "Clear Back", text_font = ( ft[0], 22, "bold" ), compound = "top",
                         corner_radius = 10, bg_color = "#d3eafc", fg_color = "#2d435b", hover_color = "#fdbf38", text_color = "white",
                         width = 230, height = 240, border_width = 0, command = lambda : change( second_page, clearBack ))
    backRem_bt_win = second_page.create_window( 190, 250, anchor = "nw", window = backRem_bt)

    # Image converter page window
    imgConvert = Imgo( r'Design\Convert_Img_logo.png', 220, 200 )
    imgConvert_bt = ctk.CTkButton( master = root, image = imgConvert, text = "Converter", text_font = ( ft[0], 22, "bold" ), compound = "top",
                         corner_radius = 10, bg_color = "#d3eafc", fg_color = "#2d435b", hover_color = "#fdbf38", text_color = "white",
                         width = 230, height = 240, border_width = 0, command = lambda : change( second_page, convertImage ))
    imgConvert_bt_win = second_page.create_window( 500, 400, anchor = "nw", window = imgConvert_bt )

    # Search image page window
    findImg = Imgo( r'Design\Find_Img_logo.png', 220, 200 )
    findImg_bt = ctk.CTkButton( master = root, image = findImg, text = "Find Image", text_font = ( ft[0], 22, "bold" ), compound = "top",
                         corner_radius = 10, bg_color = "#d3eafc", fg_color = "#2d435b", hover_color = "#fdbf38", text_color = "white",
                         width = 230, height = 240, border_width = 0, command = lambda : change( second_page, findImage ))
    findImg_bt_win = second_page.create_window( 810, 250, anchor = "nw", window = findImg_bt )

    # Sort image page window
    imgSort =Imgo( r'Design\Sort_Img_logo.png', 220, 200 )
    imgSort_bt = ctk.CTkButton( master = root, image = imgSort, text = "Sort Images", text_font = ( ft[0], 22, "bold" ), compound = "top",
                         corner_radius = 10, bg_color = "#d3eafc", fg_color = "#2d435b", hover_color = "#fdbf38", text_color = "white",
                         width = 230, height = 240, border_width = 0, command = lambda : change( second_page, sortImage ))
    imgSort_bt_win = second_page.create_window( 1120, 400, anchor = "nw", window = imgSort_bt )

    # Logout button
    log = Imgo( r'Design\logout.png', 35, 35 )
    log_bt = ctk.CTkButton( master = root, image = log, text = None, width = 45, height = 45, corner_radius = 23, 
                         bg_color = "#357adf", fg_color = "red", hover_color = "#ff5359", border_width = 0, 
                         command = lambda : change( second_page, loginPage ))
    log_bt_win = second_page.create_window( 1420, 20, anchor = "nw", window = log_bt )

    root.mainloop()

def loginPage() :

    global user,pwrd,first_page

    # Defining Structure
    first_page = Canvas( root, width = wid, height = hgt, bg = "black", highlightcolor = "#3c5390", borderwidth = 0 )
    first_page.pack( fill = "both", expand = True )

    # Background Image
    back_image = Imgo( r'Backgroud\Login_Page.jpg', 1498, 875)
    design_image = Imgo( r'Design\Login_Design.png', 600, 400)
    first_page.create_image( 0, 0, image = back_image , anchor = "nw")
    first_page.create_image( 350, 325, image = design_image, anchor = "nw")

    # Heading
    first_page.create_text( 450, 150, text = "Image Sorter", font = ( ft[0], 45, "bold" ), fill = "#1c54df" )
    first_page.create_text( 1150, 380, text = "Welcome\n    Back", font = ( ft[0], 26, "bold" ), fill = "#0b4bf5" )

    # Entry of username and password
    user = ctk.CTkEntry( master = root, placeholder_text = "Username", text_font = ( ft[1], 20 ), width = 220, height = 30, corner_radius = 14,
                        text_color = "black", fg_color = "#e1f5ff", bg_color = "#9ae2fe", border_color = "white", border_width = 3)
    pwrd = ctk.CTkEntry( master = root, placeholder_text = "Password", text_font = ( ft[1], 20 ), width = 220, height = 30, corner_radius = 14,
                        text_color = "black", fg_color = "#e1f5ff", bg_color = "#9ae2fe", border_color = "white", border_width = 3, show = "*" )

    user_win = first_page.create_window( 1015, 470, anchor = "nw", window = user )
    pwrd_win = first_page.create_window( 1015, 550, anchor = "nw", window = pwrd )

    # Login button
    log_bt = ctk.CTkButton( master = root, text = "Login", text_font = ( ft[0], 22 ), width = 50, height = 25, corner_radius = 15, 
                         text_color = "white", bg_color = "#9ae2fe", fg_color = "red", hover_color = "#ff5359", border_width = 0, 
                         command = lambda : change( first_page, menuPage))
    log_bt_win = first_page.create_window( 1090, 650, anchor = "nw", window = log_bt )

    root.mainloop()

global root
root = ctk.CTk()
root.title( "Image Sorter" )
root.iconbitmap( r'Design\Project_Icon.ico' )
root.geometry( "1200x700+200+80" )
root.resizable( False, False )
ft = [ "Tahoma", "Seoge UI", "Heloia", "Book Antiqua" ]
loginPage()