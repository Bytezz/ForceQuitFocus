#!/usr/bin/env python3
import pydbus,json,os

bus = pydbus.SessionBus()
gnome_shell = bus.get("org.gnome.Shell")

def getFocused():
	js_code = """
	var window_list = global.get_window_actors();
	var active_window_actor = window_list.find(window => window.meta_window.has_focus());
	var active_window = active_window_actor.get_meta_window()
	var vm_class = active_window.get_wm_class();
	var title = active_window.get_title();
	var pid = active_window.get_pid();
	var result = {"title": title, "appname": vm_class, "pid": pid};
	result
	"""
	
	ok,focused = gnome_shell.Eval(js_code)
	if ok:
		focused = json.loads(focused)
		return focused
	else:
		return false

def main():
	focused = getFocused()
	
	return os.system("kill -s 9 %s" % focused["pid"])


if __name__ == "__main__":
	exit(main())
