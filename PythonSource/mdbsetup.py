try:
    from robot.libraries.BuiltIn import BuiltIn
    from robot.libraries.BuiltIn import _Misc
    import robot.api.logger as logger
    from robot.api.deco import keyword
    ROBOT = False
except Exception:
    ROBOT = False

import subprocess 
import os

class mdbsetup:

    mdb_path = "C:/Program Files/Microchip/MPLABX/v6.05/mplab_platform/bin/"
    mdb_bat = "mdb.bat"
    mdb_options_path = "C:/EDrive/VSCODE/MDB/"
    mdb_options = "MDB_Command_Target.txt"
    mdb_tool = "Hwtool.txt"
    
    @keyword("Call mdb")
    def Setup_mdb_task(self, device, tool, tool_SN, hex_file):
        os.chdir("C:/EDrive/VSCODE/MDB/") 
        cmd_file = open("MDB_Command_Target.txt","w+")
        cmd_file.write("Device " + device + "\n")
        cmd_file.write("Hwtool " + tool + " " + "<sn>" + tool_SN + "\n")
        cmd_file.write("Sleep 1000 " + "\n")
        cmd_file.write("Program " + hex_file + "\n")
        cmd_file.write("Quit")
        cmd_file.close()
        #logger.console("Outside SN \n")
        mdb = os.path.join(self.mdb_path, self.mdb_bat)
        #logger.console(mdb)
        mdb_file = os.path.join(self.mdb_options_path, self.mdb_options)
        #logger.console(mdb_file)
        cmd = mdb + " " + mdb_file
        #logger.console(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc = subprocess.run(cmd, capture_output=True, text=True)
        #logger.console(proc.stdout)
        if "Program succeeded" in proc.stdout:
            logger.console("Found \n")
            return True
        else:
            return False
        # logger.console(proc.returncode)
        # if proc.returncode == 0:
        #     if "Program succeeded" in proc.stdout:
        #         logger.console("Found \n")
        #         return True
        #     else:
        #         return False
        # else:
        #     return False



    
