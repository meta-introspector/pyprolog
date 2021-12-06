import io
from .types import Variable, Term, merge_bindings, Arithmetic, Logic, FALSE
from .builtins import Write, Nl, Tab, Fail


class Rule:
    def __init__(self, head, body):
        self.head = head
        self.body = body

    def __str__(self):
        return f'{self.head}{self.body}'

    def __repr__(self):
        return str(self)


class Conjunction(Term):
    def __init__(self, args):
        super().__init__(None, *args)

    def _is_builtin(self, arg):
        if isinstance(arg, Write) or \
           isinstance(arg, Nl) or \
           isinstance(arg, Tab):
            return True
        return False

    def _is_fail(self, arg):
        if isinstance(arg, Fail):
            return True
        return False

    def query(self, runtime):
        def solutions(index, bindings):
            if index >= len(self.args):
                yield self.substitute(bindings)
            else:
                arg = self.args[index]
                if self._is_fail(arg):
                    yield FALSE()
                elif self._is_builtin(arg):
                    arg.substitute(bindings).display(runtime.stream_write)
                    yield from solutions(index + 1, bindings)
                elif isinstance(arg, Arithmetic):
                    val = arg.substitute(bindings).evaluate()
                    unified = merge_bindings(
                        {arg.var: val},
                        bindings
                    )
                    yield from solutions(index + 1, unified)
                elif isinstance(arg, Logic):
                    yield arg.substitute(bindings).evaluate()
                else:
                    for item in runtime.execute(arg.substitute(bindings)):
                        unified = merge_bindings(
                            arg.match(item),
                            bindings
                        )
                        if unified is not None:
                            yield from solutions(index + 1, unified)

        yield from solutions(0, {})

    def substitute(self, bindings):
        return Conjunction(
            map(
                (lambda arg: arg.substitute(bindings)),
                self.args
            )
        )


class Runtime:
    def __init__(self, rules):
        self.rules = rules
        self.stream = io.StringIO()
        self.stream_pos = 0

    def __del__(self):
        self.stream.close()

    def stream_write(self, text):
        self.stream.write(text)

    def stream_read(self):
        self.stream.seek(self.stream_pos)
        line = self.stream.read()
        self.stream_pos = self.stream.tell()
        return line

    def reset_stream(self):
        self.stream.seek(0)
        self.stream.truncate(0)
        self.stream_pos = 0

    def all_rules(self, query):
        if isinstance(query, Rule):
            return self.rules + [query]
        return self.rules

    def evaluate_rules(self, query, goal):
        for rule in self.all_rules(query):
            match = rule.head.match(goal)
            if match is not None:
                head = rule.head.substitute(match)
                body = rule.body.substitute(match)
                if isinstance(body, Arithmetic):
                    arith = None
                    for arg in head.args:
                        if isinstance(arg, Variable) and arg.name == body.name:
                            arith = head.substitute({arg: body.evaluate()})
                            break
                    if arith is not None:
                        yield arith
                else:
                    for item in body.query(self):
                        if not isinstance(item, FALSE):
                            yield head.substitute(body.match(item))
                        elif isinstance(item, FALSE):
                            # yield None
                            yield item

    def execute(self, query):
        goal = query
        if isinstance(query, Arithmetic):
            yield query.evaluate()
        else:
            if isinstance(query, Rule):
                goal = query.head
            yield from self.evaluate_rules(query, goal)
