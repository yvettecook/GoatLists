from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

# Even goats have things to do, so they use GoatList
# Tessa the Testing goat goes to check out the homepage
assert 'Django' in browser.title

# On the page there is a title and a header.
assert 'Goat-Do' in browser.title

# She is invited to enter a to-do list item.

# She types 'Climb up a Tree'.

# When she hits enter, the page updates, and now the page lists
# '1: Climb up a Tree' as an item on the to-do list.

# There is still a textbox inviting her to enter another to-do item
# She enters 'Don't fall off tree'.

# The page updates again, and now shows both items on her list.

# She wants to open her to-dos on another computer, and notices that the site
# has generated a unique url for her list, and there is text on the page
# explaining this.

# She visits the page in another browser window, and wow! Her todo list is there!

browser.quit
