from collections import namedtuple
import os
import subprocess as sp
from ansible.module_utils.ironration import tostr

CMD = namedtuple('Command', ['out', 'return_code'])

def which(program):
    """return absolute path of `program` or None if not in path.
    
    NOTE: like 'which', supports checking an absolute path too."""
    def is_exe(fpath):
        """True iff `fpath` points to an executable file."""
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)
    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            abs_path_candidate = os.path.join(path, program)
            if is_exe(abs_path_candidate):
                return abs_path_candidate
    return None

def sh(cmd, **kwargs):
    """return program output"""
    _disallowed_kwargs = {'shell', 'stdout', 'stderr', 'stdin'}
    if set(kwargs.keys()).intersection(_disallowed_kwargs):
        raise ValueError("invalid kwargs, you mustn't use: {}".format(_disallowed_kwargs))
    proc = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.STDOUT, shell=True, **kwargs)
    (out, err) = proc.communicate()
    return CMD(tostr(out).rstrip('\n'), proc.returncode)

def cmd_out(cmd):
    """return output from command."""
    return cmd.out

def cmd_retcode(cmd):
    """return exit code of command."""
    return cmd.return_code