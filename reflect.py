import prolog.prolog
import astor
import orjson
from prolog.parser import Parser
from prolog.scanner import Scanner
from prolog.interpreter import Runtime
import ast2json
import json

rules_text = "location(desk, office)."
tokens = Scanner(rules_text).tokenize()
rules = Parser(tokens).parse_rules()
runtime = Runtime(rules)
def add_fact(s):
    print(s)
import dumper
#orjson.dumps(tokens)
#dumper.dump(tokens)
#dumper.dump(rules)
#dumper.dump(runtime)
def dump_module(x):
    #print(x)
    if "body" in x:
        body =x["body"]
        dump_body(body)
#     print(dict(
#         #type=type(x),
#         keys=x.keys()
# #        dict=x.__dict__,
#         #str=str(x))
#     ))

def dump_dummy(x):
    #print(x)
    return
    _type = x["_type"]
    _child = x["child"]
    kys =_child.keys()
    print(_type,kys)

    #       4 With dict_keys(['_type', 'body', 'col_offset', 'end_col_offset', 'end_lineno', 'items', 'lineno', 'type_comment'])
   #    5 AsyncFunctionDef dict_keys(['_type', 'args', 'body', 'col_offset', 'decorator_list', 'end_col_offset', 'end_lineno', 'lineno', 'name', 'returns', 'type_comment'])
   #   15 Delete dict_keys(['_type', 'col_offset', 'end_col_offset', 'end_lineno', 'lineno', 'targets'])
   #   15 For dict_keys(['_type', 'body', 'col_offset', 'end_col_offset', 'end_lineno', 'iter', 'lineno', 'orelse', 'target', 'type_comment'])
   #   19 Assert dict_keys(['_type', 'col_offset', 'end_col_offset', 'end_lineno', 'lineno', 'msg', 'test'])
   #  132 Try dict_keys(['_type', 'body', 'col_offset', 'end_col_offset', 'end_lineno', 'finalbody', 'handlers', 'lineno', 'orelse'])
   #  217 AnnAssign dict_keys(['_type', 'annotation', 'col_offset', 'end_col_offset', 'end_lineno', 'lineno', 'simple', 'target', 'value'])
   #  543 If dict_keys(['_type', 'body', 'col_offset', 'end_col_offset', 'end_lineno', 'lineno', 'orelse', 'test'])
   #  643 Expr dict_keys(['_type', 'col_offset', 'end_col_offset', 'end_lineno', 'lineno', 'value'])
   # 2092 Import dict_keys(['_type', 'col_offset', 'end_col_offset', 'end_lineno', 'lineno', 'names'])
   # 2174 ClassDef dict_keys(['_type', 'bases', 'body', 'col_offset', 'decorator_list', 'end_col_offset', 'end_lineno', 'keywords', 'lineno', 'name'])
   # 2886 Assign dict_keys(['_type', 'col_offset', 'end_col_offset', 'end_lineno', 'lineno', 'targets', 'type_comment', 'value'])
   # 3721 FunctionDef dict_keys(['_type', 'args', 'body', 'col_offset', 'decorator_list', 'end_col_offset', 'end_lineno', 'lineno', 'name', 'returns', 'type_comment'])
   # 4743 ImportFrom dict_keys(['_type', 'col_offset', 'end_col_offset', 'end_lineno', 'level', 'lineno', 'module', 'names'])
def dump_ImportFrom(x):
   dump_dummy(x)
def dump_With(x):
   dump_dummy(x)
def dump_Expr(x):
   dump_dummy(x)
def dump_Import(x):
   dump_dummy(x)
def dump_Assign(x):
   dump_dummy(x)
def dump_FunctionDef(x):
   dump_dummy(x)
def dump_For(x):
   dump_dummy(x)
def dump_ClassDef(x):
    _name = x["child"]["name"]
    add_fact(f"ClassDef({_name}).")
   #dump_dummy(x)
   # 2174 ClassDef dict_keys(['_type', 'bases', 'body', 'col_offset', 'decorator_list', 'end_col_offset', 'end_lineno', 'keywords', 'lineno', 'name'])
def dump_If(x):
   dump_dummy(x)
def dump_Try(x):
   dump_dummy(x)
def dump_AnnAssign(x):
   dump_dummy(x)
def dump_Delete(x):
   dump_dummy(x)
def dump_Assert(x):
   dump_dummy(x)
def dump_AsyncFunctionDef(x):
   dump_dummy(x)

types = {
    "Module" : dump_module,
    "ImportFrom" : dump_ImportFrom,
    "With" : dump_With,
    "Expr" : dump_Expr,
    "Import" : dump_Import,
    "Assign" : dump_Assign,
    "FunctionDef" : dump_FunctionDef,
    "For" : dump_For,
    "ClassDef" : dump_ClassDef,
    "If" : dump_If,
    "Try" : dump_Try,
    "AnnAssign" : dump_AnnAssign,
    "Delete" : dump_Delete,
    "Assert" : dump_Assert,
    "AsyncFunctionDef" : dump_AsyncFunctionDef,
}
   
def dump_body(x):
    for y in x :
        _type = y["_type"]
        if _type not in types:
            print (f"    \"{_type}\" : dump_{_type},")
            print (f"def dump_{_type}(x):\n   dump_dummy(x)")
            types[_type] = dump_dummy
        else:
            types[_type](dict(parent=x,_type=_type,child=y))
            
        

def mydumper(x):
    if "_type" in x:
        _type = x["_type"]
        if _type in types:
            types[_type](x)
      
    
    
#astor.code_to_ast(Runtime.__init__)
data = astor.code_to_ast.find_py_files("./")
#dumper.dump([x for x in data])
from ast2json import ast2json
for x in data:
#    print(x)
    fname = "/".join(x)
    if "#" in fname:
        continue
    #try:
    if True:
        data = astor.code_to_ast.parse_file(fname)
        json_ast = ast2json(data)
        #print(json.dumps(dict(fname=fname,ast=json_ast)))
        # for x in json_ast
        mydumper(json_ast)
        
    #except Exception as e:
    #    pass
        
    #dumper.dump(data)
