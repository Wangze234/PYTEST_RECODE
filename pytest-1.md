被动调用

```python
 def pytest_cmdline_main():
     print("I'm hook")
```

主动调用

```python
 @pytest.hookimpl(tryfirst=True)
 def pytest_cmdline_main():
     print("I'm hook")
```

安全控制

改变测试的逻辑，失败改成功

```python
def test_api():
    assert 1 == 0
```

```python
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call():
    print("用例开始执行")
    outcome = yield
    print("用例执行失败")
    print("修改测试用例")
    outcome.force_result(1)
```

pytest中什么是通过或失败的标准

断言异常：判断为测试失败

setup异常 判断测试出错

没有异常 判断测试通过

改变测试的逻辑，成功改失败

```python
def test_api():
    assert 1 == 1
```

```python
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call():
    print("用例开始执行")
    outcome = yield
    print("用例执行失败")
    print("修改测试用例")
    assert False
```

### 创建一个新的插件

##### 1.创建项pytest-result-sender

安装pdm

使用pdm初始化项目

##### 2.编写代码

