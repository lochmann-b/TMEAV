from xml.sax import handler

class CustomerHandler(handler.ContentHandler):

    def __init__(self, line_filter):
        self.line_filter = line_filter #callback method. if true, the current line will be added to self.lines

        self.lines = [] #used to collect the result
        self.current_column = -1 #current column beeing parsed. 0 = name, 1 = email address, -1 = none
        self.current_name = '' # name found in current line
        self.current_email = '' # email address found in current line

    def startElement(self, name, attrs):
        if name == 'Row':
            # we are at the start of a row.
            # reset row related stuff
            self.current_column = -1
            self.current_name = ''
            self.current_email = ''
        elif name == 'Cell':
            # we are at the start of a column.
            # increase column index
            self.current_column += 1

    def characters(self, content):
        # we now are extracting content found between a a start tag and an end tag
        # please note that this method could be called multiple times for the same start/end tag.
        # Therefore, the content as to be appended to the current name/email address

        if self.current_column == 0:
            # append content of first column to current_name
            self.current_name += content.strip()
        elif self.current_column == 1:
            # append content of second column to current_email
            self.current_email += content.strip()

    def endElement(self, name):
        # we hit the end of a row.
        # check if the collected name / email address should be considered as invalid
        if name == "Row":
            if self.line_filter(self.current_name, self.current_email):
                self.lines.append((self.current_name, self.current_email))

    def get_lines(self):
        return self.lines