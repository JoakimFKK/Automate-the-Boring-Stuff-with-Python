## [Table for pip list](_Finished/PipList.md)

Note to self: Go through the book when you're done, and have this readme file from the getgo.
Don't put things into folders, have it in the same place.

### Chapters

<details><summary>Ch07 - Pattern Matching with Regular Expression</summary>
<p>
   
1. [Finding patterns without REGEX](_Finished/Ch7/regex_1.py)
    - Or; Why REGEX is actually a necessary evil.
2. `[PROJECT]`[Phone Numbers and Email addresses](_Finished/Ch7/regex_2.py)
    - Finds phone numbers and email addresses on the clipboard.
3. [Finding patterns with REGEX](_Finished/Ch7/regex_3.py)
    - Basic, Grouping, Piping, Optional matching, repeating, repetition, greedy & non-greedy, findall(), character class, my character class, ^ caret and $ dollar-sign, wildcard, .* dot star, newline, case insensitive, substitute

</p>
</details>

<details><summary>Ch08 - Reading and Writing Files</summary>
<p>

1. [Saving variables with shelve](_Finished/Ch8/read_1.py)
   - Shelving (With(out) `with`)
2. `[PROJECT]` [Generating random quiz.](_Finished/Ch8/read_2.py)
   - Generating 35 random tests, each question has 4 possible answers (3 wrong, 1 correct), and an accompanying answer key, with an indicator as to which one it corresponds to.
3. [Multi-clipboard](_Finished/Ch8/read_3.py) **[DOESN'T WORK]**

</p>
</details>

<details><summary>Ch09 - Organising Files</summary>
<p>

1. [Shutil](_Finished/Ch9/organise_1.py)
   - Creating a backup.
   - Moving files.
   - Deleting files.
2. [Send2Trash Module](_Finished/Ch9/organise_2.py)
   - Deleting with Send2Trash.
3. [ZIP files.](_Finished/Ch9/organise_3.py)
   - Reading and printing the contents of a zip-file.
   - Extracting a zip-file.
   - Extracting a specific element from a zip-file.
   - Creating a zip-file.
   - Adding content to a zip-file.
4. `[PROJECT]` [American/Europe Date](_Finished/Ch9/organise_4.py)
   - Changing filenames from American dates (MM-DD-YYYY) to European (DD-MM-YYYY).
   - _Potentially broken, not sure if I named the files correctly._
5. `[PROJECT]` [ZIP Backup](_Finished/Ch9/organise_5.py)
   - Backups an entire folder and its content into a zipfile whose name increments.

</p>
</details>

<details><summary>Ch10 - Debugging</summary>
<p>

1. [Logging](_Finished/Ch10/debug_1.py)
   - Introduction to logging.
2. `[PROJECT]` [Debugging Cointoss](_Finished/Ch10/debug_2.py)
   - No programming involved, just pointing out bugs.

</p>
</details>

<details><summary>Ch11 - Web Scraping</summary>
<p>

1. [MapIt](_Finished/Ch11/web_1.py)
   - Takes an argument, and opens up the default webbrowser to the location given.
2. [Requests](_Finished/Ch11/web_2.py)
   - Downloading a page and accessing its data.
   - Checking for errors.
3. [Saving downloaded files](_Finished/Ch11/web_3.py)
   - Downloading the entire Gutenberg version of 'Romeo and Juliet'.
4. [Beautiful Soup](_Finished/Ch/web_4.py)
   - Downloading with beautifulsoup
   - Loading an HTML file with beautiful soup.
   - Finding an element with the `select()` method
   - Getting data from an element's attributes.
5. `[PROJECT]` [I'm Feeling Lucky!](_Finished/Ch11/web_5.py) **[DOESN'T WORK AS INTENDED]**
   - Get and open X amount of search results from google.
   - ISSUES:
     - The code that beautifulsoup gets compared to what you can see in `inspect element` is widely different.
     - Technically it works, but not as intended.
6. [download_xkcd.py](_Finished/Ch11/download_xkcd.py)
   - `[PROJECT]` Downloading Every XKCD Comic
7. **[DO AT HOME]** [firefox.py](_Finished/Ch11/firefox.py)
   - P. 256.
   - Controlling the browser with the selenium module.

</p>
</details>

<details><summary>Ch12 - Working With Excel Spreadsheets</summary>
<p>

1. [intro.py](_Finished/Ch12/intro.py)
   - Import the openpyxl module.
   - Call the openpyxl.load_workbook() function.
   - Get a workbook object.
   - Call the _.active_ or sheet*[]* workbook _functions_.
2. [get_multiple_cells.py](_Finished/Ch12/get_multiple_cells.py)
   - Use indexing or cell() sheet method with row and column keyword arguments.
   - Get a cell object.
   - Read the cell object's value attribute.
3. [read_census_excel.py](_Finished/Ch12/read_census_excel.py)
   - `[PROJECT]` "You have the boring task of going through its thousands of rows to count both the total population and the number of census tracts for each county.
4. [writing_excel_documents.py](_Finished/Ch12/writing_excel_documents.py)
    - Creating and saving Excel documents.
    - Creating and removing sheets.
    - Writing values to cells.
5. [Updating a spreadsheet](_Finished/Ch12/update_spreadsheet.py)
    - `[PROJECT]` In this project, you’ll write a program to update cells in a spreadsheet of produce sales. Your program will look through the spreadsheet, find specific kinds of produce, and update their prices. 
6. [Styling a spreadsheet](_Finished/Ch12/styling.py)
    - How to make a font object and how to apply it.
7. [Formulas](_Finished/Ch12/formulas.py)
    - How to make formulas.
8. [Adjusting Rows and Columns](_Finished/Ch12/rowandcolumns.py)
    - Adjusting row and column sizes.
    - Merge and unmerge cells.
    - Freezing panes.
9. [Charts](_Finished/Ch12/charts.py)
    - Make a bar-chart.
    - If more is needed, check the documentation.
10. [Multiplication Table](_Finished/Ch12/multiplicationTable.py)
    - Make a multiplication table that takes an input, bolds the outer lines, and does the math.


</p>
</details>

<details><summary>Ch13 - Working With PDF and Word Documents</summary>
<p>

1. [Introduction](_Finished/Ch13/intro.py)
    - PdfFileReader
2. [Decrypting PDFs](_Finished/Ch13/decrypt.py)
    - Decrypting PDF.
3. [Creating PDFs](_Finished/Ch13/create_pdf.py)
    - **NOT DOING IT** It's already been done in Basic Python.
4. [Word Documents](_Finished/Ch13/word_documents.py)
5. [Getting the full text from a .docx file](_Finished/Ch13/full_text.py)
    - Getting the full text from a docx file.
6. [Running local module](_Finished/Ch13/get_full_text.py)
    - Importing [full_text.py](_Finished/Ch13/full_text.py) and running the script.
7. [Styling paragraph and run objects](_Finished/Ch13/styling_text.py)
    - **NOTE!** The book is outdated, and is not a representative of the current version of python-docx.
8. [Writing Word Documents](_Finished/Ch13/writing_word_documents.py)
    - Create a simple word document.
    - Create a simple word document with multiple paragraphs.
    - Add headings to a word document.
    - Adding line and page breaks.
    - Adding pictures.

</p>
</details>

<details><summary>Ch14 - Working with CSV Files and JSON Data</summary>
<p>

1. CSV
    1. [The csv Module](_Finished/Ch14/csv_module.py)
        - Opening and reading.
    2. [Reading Data from Reader Objects in a `for` Loop](_Finished/Ch14/csv_loop_read.py)
    3. [Writer Objects](_Finished/Ch14/csv_writer.py)
    4. [The `delimiter` and `lineterminator` Keyword Arguments](_Finished/Ch14/csv_delimiter_lineterminator.py)
    5. `[PROJECT]` [Removing the header of CSV files](_Finished/Ch14/remove_csv_header.py)
2. JSON
    1. [JSON and APIs](_Finished/Ch14/json_intro.py)
        - Intro to JSON module.
    2. [Writing Json with the `dumps()`](_Finished/Ch14/json_dumps.py)
    3. `[PROJECT]` [Fetching current weather data](_Finished/Ch14/quick_weather.py)
        - Needs API key

</p>
</details>

<details><summary>Ch15 - Keeping Time, Scheduling Tasks, And Launching Programs</summary>
<p>

1. [The `time` module](_Finished/Ch15/time_module.py)
    - `time.time()`
    - How to get the time it takes for a function to run.
    - `time.sleep()`
    - Rounding numbers.
2. `[PROJECT]` [Super Stopwatch](_Finished/Ch15/super_stopwatch.py)
    1. The program will do:
        - Track the amount of time elapsed between presses of the `ENTER` key, with each press starting a new "lap" onthe timer.
        - Print the lap number, total time, and lap time.
    2. The code will need to do:
        - Find the current time by calling `time.time()` and store it as a timestamp at the start of the program, as well as at the start of each lap.
        - Keep a lap coutner and increment it every time the user presses `ENTER`.
        - Calculate the elapsed time by subtracting timestamps.
        - Handle the `KeyboardInterrupt` exception so the user can press `CTRL-C` to quit. 
3. [The `datetime` Module](_Finished/Ch15/datetime_module.py)
    - Intro to `datetime` and `datetime.datetime`
4. [The `timedelta` Data Type](_Finished/Ch15/timedelta_data.py)
    - Intro to `datetime.timedelta`
5. [Pausing until a specific date](_Finished/Ch15/time_sleep.py)
    - Intro to `time.sleep()`
6. [Converting `datetime` Objects into Strings](_Finished/Ch15/date_strings.py)
    - How to convert a `datetime` object into a readable format
7. [Multithreading](_Finished/Ch15/multithreading.py)
    - Intro to `threading` and multithreading
8. [Multithreaded XKCD Downloader](_Finished/Ch15/xkcd_downloader.py)
    - Expanded version of [download_xkcd.py](_Finished/Ch11/download_xkcd.py), where `threading` is used to make the process faster.
9. [Launching Other Programs from Python](_Finished/Ch15/launching_programs.py)
    - Run program
    - Run and wait
    - Passing command line arguments to Popen()
    - Opening files with default applications
10. [Running Other Python Scripts](_Finished/Ch15/multitrack_programming.py)
11. [Project: Simple Countdown Program](_Finished/Ch15/simple_countdown_program.py)

</p>
</details>

<details><summary>Ch16 - Sending Email and Text Messages</summary>
<p>

Note! The book is horrible outdated on this topic, and should be be taken with a grain of salt.

1. [Sending Email](_Finished/Ch16/sending_email.py)
    - Check to see if there's connection to the SMTP server
    - Login
    - Send mail
2. [IMAP](_Finished/Ch16/retrieving_and_deleting_emails.py)
    - Read documentation.

</p>
</details>

<details><summary>Ch17 - Manipulating Images</summary>
<p>

1. [Pillow RGBA intro](_Finished/Ch17/rgba_test.py)
2. [Coordinates and Box Tuples](_Finished/Ch17/coordinates_and_box_tuples.txt)
3. [Manipulating images with Pillow](_Finished/Ch17/manipulating_imgs.py)
    - Working with Image data type
    - Creating a new image
    - Cropping images
    - Copying and pasting images onto other images
    - Resizing an Image
    - Rotating and flipping images
    - Changing individual pixels
4. Project: [Adding a logo](_Finished/Ch17/adding_logo.py)
5. [Drawing on images](_Finished/Ch17/drawing_on_images.py)


</p>
</details>

<details><summary>Ch18 - Controlling The Keyboard and Mouse With GUI Automation</summary>
<p>

1. [pyautogui Module](Ch18/pyautogiu_module.py)
2. [Project: Where is your mouse right now?](Ch18/mouse_now.py)
3. [Clicking the mouse](Ch18/click_mouse.py)
4. [Dragging the mouse](Ch18/drag_mouse.py)
5. [Draw a spiral](Ch18/spiral_draw.py)
6. [Scrolling the Mouse](Ch18/scrolling_mouse.py)
7. [Screenshots](Ch18/getting_a_screenshot.py)
8. [Analyzing the Screenshot](Ch18/analyzing_the_screenshot.py)
9. [Project: Extended 'Where is your mouse right now?](Ch18/extend_mouse_now.py)
10. [Image Recognition](Ch18/image_recognition.py)

</p>
</details>
