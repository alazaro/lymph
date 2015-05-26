import six

from lymph.cli.base import Command, get_command_classes


class ListCommand(Command):
    """
    Usage: lymph list [options]

    {COMMON_OPTIONS}
    """

    short_description = 'List available commands.'
    needs_config = False

    def run(self):
        command_names = get_command_classes().keys()
        max_command_name = max(command_names, key=len)
        description_offset = len(max_command_name) + 2
        for name, cls in six.iteritems(get_command_classes()):
            print(u'{t.bold}{name:<{offset}}{t.normal}{description}'.format(
                t=self.terminal,
                name=name,
                description=cls.short_description,
                offset=description_offset
            ))

