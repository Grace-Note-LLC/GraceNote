import flet
 
 
def main(page:Page):
 
	# FIRST INITIAL YOU DEFAULT MODE LIGHT OR DARK
	page.theme_mode = "light"
 
	# ADD PROGESSBAR EFFECT WHEN CHANGE LIGHT OR DARK
	# THIS OPTIONAL
	page.splash = ProgressBar(visible=False)
 
 
	def changetheme(e):
		page.splash.visible = True
		page.theme_mode = "light" if page.theme_mode =="dark" else "dark"
		page.update()
 
		# DELAY EFFECT THE ANIMATION
		time.sleep(0.5)
 
		# CHANGE THE ICON DARK MODE OR LIGHT MODE
		toggledarklight.selected = not toggledarklight.selected
 
		# AND DISABLE AGAIN THE PROGRESSBAR WHEN CHANGE DARK MODE
		page.splash.visible = False
 
		# AND PAGE UPDATE FOR CHANGE STATE
		page.update()
 
	# CREATE TOGLE BUTTON DARK MODE LIGHT
	toggledarklight = IconButton(
		on_click=changetheme,
		icon="dark_mode",
		selected_icon="light_mode",
		style=ButtonStyle(
			# change color if light and dark
			color={"":colors.BLACK,"selected":colors.WHITE}
 
			)
 
		)
 
	page.add(
		AppBar(
		title=Text("Hello",size=30),
		bgcolor="blue",
		leading=IconButton(icon="menu"),
		actions=[
		toggledarklight 
 
		]
			),
		# THE CONTENT YOU
		Column([
		Text("Hello From YOUTUBE ",size=30)
 
			])
 
		)
 
 
 
flet.app(target=main)