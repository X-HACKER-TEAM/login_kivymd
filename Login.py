from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
import sys
KV='''
MDScreen:
	md_bg_color:0.7,.6,.9,.9
	MDToolbar:
	#	radius:[dp(10)]
		elevation:10
		title:"My App"
		pos_hint:{'top':1}
		left_action_items:[["menu",lambda x:x]]
		right_action_items:[["moon-waning-crescent",lambda x:app.ThemeMode(x)]]
		md_bg_color:[35/255,49/255,48/255,1]	
	MDCard:
		radius:[dp(100)]
		size_hint:None,None
		size:500,500
		pos_hint:{"center_x":.5,"center_y":.5}
		elevation:15
		padding:20
		spacing:30
		orientation:"vertical"
		md_bg_color:[35/255,49/255,48/255,1]
		MDLabel:
			text:"Login"
			font_style:'Button'
			font_size:70
			halign:"center"
			size_hint_y:None
			height:self.texture_size[1]
		MDTextFieldRound:
			hint_text:"username"
			icon_left:"account"
			size_hint_x:None
			width:330
			font_size:20
			pos_hint:{"center_x":.5}
		MDTextFieldRound:
			radius:[dp(100)]
			hint_text:"password"
			icon_right:"eye-off"
			icon_left:"key"
			size_hint_x:None
			width:330
			font_size:20
			pos_hint:{"center_x":.5}
		MDRoundFlatButton:
			text:"Login"
			size_hint:None,None
			pos_hint:{"center_x":0.5,"center_y":0.5}
								
'''
class App(MDApp):
	def build(self):
		self.theme_cls.theme_style="Light"
		return Builder.load_string(KV)
	def ThemeMode(self,*args):
		t=self.theme_cls.theme_style
		t="Light" if t!="Light" else "Dark"
		self.theme_cls.theme_style=t
App().run()		