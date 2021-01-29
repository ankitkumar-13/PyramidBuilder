# PyramidBuilder
Make an pyramid app only by using HTML, CSS &amp; Javascript. This automatically creates code and configures the file.

As wrote above, anyone can easily develop an app using HTML, CSS and Javascript knowledge. You can use CSS, and Javascript if you want, else neglect them, pure html can also be used to develop an pyramid app, or more precisely a webapp.

- #### And make sure you have python installed on your device.

------------

# Installing needed Modules :-
Before going to use the PyramidBuilder, you need to install some modules.
- Go to the Command Line:-  
>On Windows :-  
>  
>Press the Start Menu Button.  
>Search by typing cmd.  
>Click on the app named Command Prompt


- Use the pip command :-
>On Windows :-  
>  
>Type the following command :-  
>```cmd
>pip install PySimpleGUI BeautifulSoup4
>```

##### Some code will be executed there.
##### This is all you need for executed PyramidBuilder.

------------

# Configuration that You Need to Do :-
Due to some reasons, such as time unavailability, some configuration you also need to do.
Although in some future update, this feature will be automatic (Hoping Soon!).
Till then, manual configuration has to be done.
  
In HTML files, **Images should be in Base64 format**(textual),  
For example, if you have an image link, i.e. `<img src='Folder/SubFolder/abc.png' width=300 height=550>` then it should be changed as, `<img src='data:image/png';base64, code'>`, you can get it converted through many websites such as  CodeBeautify on `https://codebeautify.org/image-to-base64-converter`.
There you can get the Base64 code, complete `<img>` tag with everything done is also provided.
Now handling large Base64 Code can be done using Notepad. Since its smoother while handling such large code.

Now, links,
Linking should be done in the following way :-
A Normal hyperlink to another HTML file, i.e., `<A href="Template/Pages/abc.html"> Some Text </A>` should be written as `<A href='/abc.html'>` only.
Forward slash and file name with extension is needed `<A href='/FileName.html'>Some Text </A>`.

That's enough.

------------

# Steps to create an App :-
Simply, prepare HTML files using inline CSS and <script> tag for Javascript on the same HTML file. Multiple files can be used but individual CSS and Javascript for them should be in the same file in which you have HTML.

- #### You have to download the PyramidBuilder.py file from this repository. Though repository may be a big word, simply download the file from the main branch.(above 👆)
- #### Then,  the only think you to do is to double-click on it and further the program is self explanatory. It's a GUI based program, so you  don't have to worry about learning to code.

# A Tutorial:
#### On the Starting screen you will see :-
<p align="center">
  <img src="ReadmeStaticContent/Screen1.png"><br>  
  Starting Screen.
</p>

- Click on Browse Button.
- Choose a File.
- Click Next File.
- Browse Another File.
##### When You are done choosing all the files press Submit All button.


Next, You will see a screen like :-
<p align="center">
  <img src="ReadmeStaticContent/Screen2.png"><br>  
  Folder Choosing Screen.
</p>
