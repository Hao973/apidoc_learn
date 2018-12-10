# -*- coding: UTF-8 -*-

def add_func(x, y):
    """
    @apiGroup Add_Func
    @api {add_func} /myapidoc add_func函数
    @apiName AddFunc
    @apiDescription add x and y
    @apiParam {Number} x=0 x
    @apiParam {Number} y=0 y
    @apiSuccess {Number} add_x_y x+y
    """
    return x + y

if __name__ == "__main__":
    """
    @apiGroup Main
    @api {main} /myapidoc main函数
    """
    print 'ApiDoc Test'
    exit(0)
