import prolog.prolog
import pprint
import astor
from ast2json import ast2json
import orjson
from prolog.parser import Parser
from prolog.scanner import Scanner
from prolog.interpreter import Runtime
import ast2json
import json
import dumper

def example_prolog():
    rules_text = "location(desk, office)."
    tokens = Scanner(rules_text).tokenize()
    rules = Parser(tokens).parse_rules()
    runtime = Runtime(rules)
    
def add_fact(s):
    tokens = Scanner(s).tokenize()
    rules = Parser(tokens).parse_rules()
    #dumper.dump(tokens)
    #dumper.dump(rules)    
    print(s)

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

### only in function body
def dump_Global(x):
   dump_dummy(x)
def dump_Nonlocal(x):
   dump_dummy(x)
def dump_Raise(x):
   dump_dummy(x)
def dump_Return(x):
   dump_dummy(x)
def dump_AugAssign(x):
   dump_dummy(x)
def dump_While(x):
   dump_dummy(x)
def dump_Match(x):
   dump_dummy(x)


def dump_dummy(x):
    _type = x["_type"]
    _source = x["_source"]
    print("Dump",_type,_source)
    #return
    _ptype = x["car"]

    _cdr = x["cdr"]
    kys =_cdr.keys()
    #raise Exception(str(x.keys()))
    # print(dict(car=_ptype,
    #           type=_type,
    #           keys=kys))

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
    #dump_dummy(x)
    #pprint.pprint(x['cdr'].keys())
    #dict_keys(['_type', 'args', 'body', 'col_offset', 'decorator_list', 'end_col_offset', 'end_lineno', 'lineno', 'name', 'returns', 'type_comment'])
    function_body = x['cdr']['body']
    function_name = x['cdr']['name']
    args = x['cdr']['args']
    _return = x['cdr'].get('return',None)
    type_comment = x['cdr']['type_comment']
    for y in function_body:
        _type = y["_type"]
        if _type not in types:
            print (f"    \"{_type}\" : dump_{_type},")
            print (f"def dump_{_type}(x):\n   dump_dummy(x)")
            types[_type] = dump_dummy
        else:
            
            types[_type](
                dict(
                    car=function_name,
                    _source="function_body",
                    _type=_type,
                    cdr=y
                )
            )
    
def dump_For(x):
   dump_dummy(x)

def dump_ClassDef_bases(x):
    car=x['car']
    name=x['name']
    bases=x['bases']
    for x in bases:
        if "id" in x:
            add_fact(f"class_def_base(\'{name}\',\'{x['id']}\').")
        elif "attr" in x:
            add_fact(f"class_def_base(\'{name}\',\'{x['attr']}\').")
        #else:
            #BASES2 Url {'_type': 'Call', 'args': [{'_type': 'Constant', 'col_offset': 21, 'end_col_offset': 26, 'end_lineno': 82, 'kind': None, 'lineno': 82, 'n': 'Url', 's': 'Url', 'value': 'Url'}, {'_type': 'Name', 'col_offset': 28, 'ctx': {'_type': 'Load'}, 'end_col_offset': 37, 'end_lineno': 82, 'id': 'url_attrs', 'lineno': 82}], 'col_offset': 10, 'end_col_offset': 38, 'end_lineno': 82, 'func': {'_type': 'Name', 'col_offset': 10, 'ctx': {'_type': 'Load'}, 'end_col_offset': 20, 'end_lineno': 82, 'id': 'namedtuple', 'lineno': 82}, 'keywords': [], 'lineno': 82}
            #BASES2 _SecretBase {'_type': 'Subscript', 'col_offset': 18, 'ctx': {'_type': 'Load'}, 'end_col_offset': 37, 'end_lineno': 1456, 'lineno': 1456, 'slice': {'_type': 'Name', 'col_offset': 26, 'ctx': {'_type': 'Load'}, 'end_col_offset': 36, 'end_lineno': 1456, 'id': 'SecretType', 'lineno': 1456}, 'value': {'_type': 'Name', 'col_offset': 18, 'ctx': {'_type': 'Load'}, 'end_col_offset': 25, 'end_lineno': 1456, 'id': 'Generic', 'lineno': 1456}}
            #print("BASES2",name,x)
    #dict(car=x,bases=_bases))

#        
def dump_Pass(x):
   dump_dummy(x)

def dump_ClassDef_body(x):
    _car = x["car"]
    class_name = x["class_name"]
    _body = x["body"]
    for y in _body:
        _type = y["_type"]
        if _type not in types:
            print (f"    \"{_type}\" : dump_{_type},")
            print (f"def dump_{_type}(x):\n   dump_dummy(x)")
            types[_type] = dump_dummy
        else:
            
            types[_type](
                dict(
                    car=class_name,
                    _source="class_body",
                    _type=_type,
                    cdr=y
                )
            )

def dump_ClassDef(x):
    _name = x["cdr"]["name"]
    add_fact(f"class_def(\'{_name}\').")

    _bases = x["cdr"]["bases"]
    dump_ClassDef_bases(dict(car=x,
                             name=_name,
                             bases=_bases))
    _body = x["cdr"]["body"]
    dump_ClassDef_body(
        dict(car=x,
             class_name=_name,
             body=_body))
    _keywords = x["cdr"]["keywords"]
    
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

# from function body
    "Raise" : dump_Raise,
    "Return" : dump_Return,
    "AugAssign" : dump_AugAssign,
    "While" : dump_While,
    "Global" : dump_Global,
    "Nonlocal" : dump_Nonlocal,
    "Match" : dump_Match,
###
    "Pass" : dump_Pass,
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
            types[_type](dict(
                _source="module",
                car=x,
                _type=_type,cdr=y))
                    
def mydumper(x):
    if "_type" in x:
        _type = x["_type"]
        if _type in types:
            types[_type](x)
             
def collect_project_files():
    data = astor.code_to_ast.find_py_files("./")
    for x in data:
        fname = "/".join(x)
        if "#" in fname: # ignore temp files with #
            continue

        data = astor.code_to_ast.parse_file(fname)
        json_ast = ast2json(data)
        #print(json.dumps(dict(fname=fname,ast=json_ast)))
        # for x in json_ast
        #mydumper(json_ast)
        yield json_ast
        
