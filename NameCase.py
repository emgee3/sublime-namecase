import sublime
import sublime_plugin
import subprocess
 
class NameCaseCommand(sublime_plugin.TextCommand):
 
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                region = self.view.line(region)

            p = subprocess.Popen(
                "namecase",
                shell   = True,
                bufsize = -1,
                stdout  = subprocess.PIPE,
                stderr  = subprocess.PIPE,
                stdin   = subprocess.PIPE)
     
            output, error = p.communicate(self.view.substr(region).encode('utf-8'))
     
            if error:
                sublime.errorMessage(error.decode('utf-8'))
            else:
                self.view.replace(edit, region, output.decode('utf-8'))
