# django-internetdefenseleague #
That's a lot to type. Sorry.

## What is this? ##
The [Internet Defense League](http://internetdefenseleague.org) is an organization which organizes web protests against legislation such as SOPA which threaten the ability to use the internet and web.
This is an app which provides some simple Django template tags to insert the JavaScript and HTML to join the network and help the cause while also providing a per site toggle in settings.py
so that the templates which reference these tags can be used on sites which you don't want to participate as well.

## Usage ##
- Install django-internetdefenseleague
- Add `internetdefenseleague` to your `INSTALLED_APPS`
- Add `DEFENSE_LEAGUE = True` to your settings.py
- Add the template tags to your Django templates

Examples of what the following tags display can be viewed [here](http://members.internetdefenseleague.org/).

## Template Tags ##
### `{% idl_popup "modal"|"banner" %}` ###
adds the JavaScript to display the main popup or banner when the league enables a campaign

### `{% idl_super_badge %}` ###
Displays the super badge

### `{% idl_shield_badge %}` ###
Displays the shield badge

### `{% idl_sidebar_badge %}` ###
Displays the sidebar badge

### `{% idl_footer_badge %}` ###
Displays the footer badge

### `{% idl_left_ribbon %}` ###
Displays the left ribbon

### `{% idl_right_ribbon %}` ###
Displays the right ribbon
