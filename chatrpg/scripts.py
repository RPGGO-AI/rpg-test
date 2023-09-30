import logging
import os
import re

from chatrpg.utils import log_and_print_online
import difflib

class Scripts:
    def __init__(self, generated_content=""):
        self.directory: str = None
        self.version: float = 1.0
        self.generated_content: str = generated_content
        self.scriptbooks = {}

        def extract_filename_from_line(lines):
            file_name = ""
            for candidate in re.finditer(r"(\w+\.\w+)", lines, re.DOTALL):
                file_name = candidate.group()
                file_name = file_name.lower()
            return file_name

        def extract_filename_from_scene(code):
            logging.debug("extract name")
            logging.debug(code)
            # file_name = ""
            # regex_extract = r"class (\S+?):\n"
            # matches_extract = re.finditer(regex_extract, code, re.DOTALL)
            # for match_extract in matches_extract:
            #     file_name = match_extract.group(1)
            # file_name = file_name.lower().split("(")[0] + ".md"
            # return file_name
            return "unknown.md"

        if generated_content != "":
            regex = r"(.+?)\n```.*?\n(.*?)```"
            matches = re.finditer(regex, self.generated_content, re.DOTALL)
            for match in matches:
                code = match.group(2)
                if "SCRIPT" in code:
                    continue
                group1 = match.group(1)
                filename = extract_filename_from_line(group1)
                # if "__main__" in code:
                #     filename = "main.md"
                if filename == "":  # post-processing
                    filename = extract_filename_from_scene(code)
                assert filename != ""
                if filename is not None and code is not None and len(filename) > 0 and len(code) > 0:
                    self.scriptbooks[filename] = self._format(code)

    def _format(self, code):
        code = "\n".join([line for line in code.split("\n") if len(line.strip()) > 0])
        return code

    def _update(self, generated_content):
        new_codes = Scripts(generated_content)
        differ = difflib.Differ()
        for key in new_codes.scriptbooks.keys():
            if key not in self.scriptbooks.keys() or self.scriptbooks[key] != new_codes.scriptbooks[key]:
                update_codes_content = "**[Update Codes]**\n\n"
                update_codes_content += "{} updated.\n".format(key)
                logging.debug("diff key is " + key)
                logging.debug(self.scriptbooks.keys())
                old_codes_content = self.scriptbooks[key] if key in self.scriptbooks.keys() else "# None"
                new_codes_content = new_codes.scriptbooks[key]

                lines_old = old_codes_content.splitlines()
                lines_new = new_codes_content.splitlines()

                unified_diff = difflib.unified_diff(lines_old, lines_new, lineterm='', fromfile='Old', tofile='New')
                unified_diff = '\n'.join(unified_diff)
                update_codes_content = update_codes_content + "\n\n" + """```
'''

'''\n""" + unified_diff + "\n```"

                log_and_print_online(update_codes_content)
                self.scriptbooks[key] = new_codes.scriptbooks[key]

    def _rewrite(self, git_management) -> None:
        directory = self.directory
        rewrite_codes_content = "**[Rewrite Codes]**\n\n"
        if os.path.exists(directory) and len(os.listdir(directory)) > 0:
            self.version += 1.0
        if not os.path.exists(directory):
            os.mkdir(self.directory)
            rewrite_codes_content += "{} Created\n".format(directory)

        for filename in self.scriptbooks.keys():
            filepath = os.path.join(directory, filename)
            with open(filepath, "w", encoding="utf-8") as writer:
                writer.write(self.scriptbooks[filename])
                rewrite_codes_content += os.path.join(directory, filename) + " Wrote\n"

        if git_management:
            if self.version == 1.0:
                os.system("cd {}; git init".format(self.directory))
            os.system("cd {}; git add .".format(self.directory))
            os.system("cd {}; git commit -m \"{}\"".format(self.directory, self.version))

        log_and_print_online(rewrite_codes_content)

    def _get(self) -> str:
        content = ""
        for filename in self.scriptbooks.keys():
            content += "{}\n```{}\n{}\n```\n\n".format(filename,
                                                       "english" if filename.endswith(".md") else filename.split(".")[
                                                           -1], self.scriptbooks[filename])
        return content

    def _load_from_hardware(self, directory) -> None:
        assert len([filename for filename in os.listdir(directory) if filename.endswith(".md")]) > 0
        for root, directories, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith(".md"):
                    code = open(os.path.join(directory, filename), "r", encoding="utf-8").read()
                    self.scriptbooks[filename] = self._format(code)
        log_and_print_online("{} files read from {}".format(len(self.scriptbooks.keys()), directory))
