#coding:utf-8
import unittest
import assertpy
class Tassert(unittest.TestCase):
    #预期结果与实际结果断言
    def assert_value_valid(self,value, tovalue):
        assertpy.assert_that(value).is_equal_to(tovalue)
        #check value's was equal to value's
    def assert_value_invalid(self,value,tovalue):
        assertpy.assert_that(value).is_not_equal_to(tovalue)
    def assert_contains_in(self,value,tovalue):
        assertpy.assert_that(value).contains(tovalue)

    #单个数据断言
    def assert_is_empty(self,value):
        assertpy.assert_that(value).is_empty()#是空
    def assert_is_ex(self,value):
        assertpy.assert_that(value).exists()#存在
    def assert_is_true(self,value):
        assertpy.assert_that(value).is_true()
    def assert_is_false(self,value):
        assertpy.assert_that(value).is_false()
    def assert_is_none(self,value):
        assertpy.assert_that(value).is_none()
    def assert_is_not_none(self,value):
        assertpy.assert_that(value).is_not_none()#不是null
    def assert_is__type_of_str(self,value): #判断数据类型，暂时不用
        assertpy.assert_that(value).is_type_of(value,list)
    def runTest(self):
        pass
if __name__ == '__main__':
    test = Tassert()
    test.assert_value_valid('1','1')
