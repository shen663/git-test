"""
多功能计算器程序
支持：基本运算、表达式计算、历史记录、进制转换
"""

import math

class Calculator:
    """计算器类，支持基本四则运算、括号、幂运算、科学计算等"""

    def __init__(self) -> None:
        self.history: list[str] = []  # 运算历史记录
        self.result: float = 0.0

    # ---- 基本运算 ----
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("除数不能为零！")
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
        return a ** b

    @staticmethod
    def sqrt(a: float) -> float:
        if a < 0:
            raise ValueError("不能对负数开平方根！")
        return math.sqrt(a)

    # ---- 表达式求值 ----
    def evaluate(self, expression: str) -> float:
        """
        计算数学表达式。
        支持：+, -, *, /, //, %, **, sqrt(), sin(), cos(), tan(), log(), abs(), pi, e
        """
        # 安全检查：内部使用受限命名空间执行
        expr_clean = expression.strip()
        if not expr_clean:
            raise ValueError("表达式不能为空！")

        # 将中文字符替换为英文
        expr_clean = (expr_clean
                      .replace('（', '(')
                      .replace('）', ')')
                      .replace('×', '*')
                      .replace('÷', '/')
                      .replace('＋', '+')
                      .replace('－', '-')
                      .replace('＾', '**')
                      .replace('％', '%'))

        # 构建安全的命名空间
        safe_dict = {
            "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos,
            "tan": math.tan, "log": math.log, "log10": math.log10,
            "log2": math.log2, "abs": abs, "round": round,
            "pi": math.pi, "e": math.e, "ceil": math.ceil,
            "floor": math.floor, "factorial": math.factorial,
        }
        result = eval(expr_clean, {"__builtins__": {}}, safe_dict)
        self.result = result
        self.history.append(f"{expression} = {result}")
        return result

    # ---- 交互式菜单 ----
    def interactive_menu(self) -> None:
        """交互式计算器模式"""
        while True:
            print("\n" + "=" * 42)
            print("          多 功 能 计 算 器")
            print("=" * 42)
            print("  1. 直接输入数学表达式")
            print("  2. 基本四则运算（逐步选择）")
            print("  3. 科学计算")
            print("  4. 进制转换")
            print("  5. 查看历史记录")
            print("  6. 清除历史记录")
            print("  7. 退出程序")
            print("=" * 42)

            choice = input("请选择功能 (1-7): ").strip()

            if choice == "1":
                self._expr_calc()
            elif choice == "2":
                self._basic_calc()
            elif choice == "3":
                self._scientific_calc()
            elif choice == "4":
                self._base_converter()
            elif choice == "5":
                self._show_history()
            elif choice == "6":
                self.history.clear()
                print("✅ 历史记录已清除！")
            elif choice == "7":
                print("👋 感谢使用，再见！")
                break
            else:
                print("⚠️ 无效选择，请输入 1-7 之间的数字。")

    def _expr_calc(self) -> None:
        """表达式计算"""
        print("\n📐 支持运算: + - * / // % ** | 函数: sqrt sin cos tan log abs")
        print("   常量: pi e | 示例: 2 + 3 * 4, sqrt(16), sin(pi/2)")
        expr = input("请输入数学表达式: ").strip()
        try:
            result = self.evaluate(expr)
            print(f"📝 结果: {result}")
        except Exception as e:
            print(f"❌ 错误: {e}")

    def _basic_calc(self) -> None:
        """逐步选择的基本运算"""
        ops = {
            "1": ("加法 +", self.add),
            "2": ("减法 -", self.subtract),
            "3": ("乘法 ×", self.multiply),
            "4": ("除法 ÷", self.divide),
            "5": ("幂运算 ^", self.power),
        }
        print("\n选择运算类型:")
        for k, (name, _) in ops.items():
            print(f"  {k}. {name}")

        op_choice = input("请选择 (1-5): ").strip()
        if op_choice not in ops:
            print("⚠️ 无效选择！")
            return

        try:
            a = float(input("请输入第一个数: ").strip())
            b = float(input("请输入第二个数: ").strip())
            name, func = ops[op_choice]
            result = func(a, b)
            self.result = result
            expr = f"{a} {name[-1]} {b} = {result}"
            self.history.append(expr)
            print(f"📝 {expr}")
        except ValueError:
            print("❌ 请输入有效的数字！")
        except ZeroDivisionError as e:
            print(f"❌ {e}")

    def _scientific_calc(self) -> None:
        """科学计算"""
        ops = {
            "1": ("开平方根 √x", lambda x: self.sqrt(x)),
            "2": ("正弦 sin(x)", lambda x: math.sin(math.radians(x))),
            "3": ("余弦 cos(x)", lambda x: math.cos(math.radians(x))),
            "4": ("正切 tan(x)", lambda x: math.tan(math.radians(x))),
            "5": ("自然对数 ln(x)", lambda x: math.log(x)),
            "6": ("常用对数 log10(x)", lambda x: math.log10(x)),
            "7": ("阶乘 x!", lambda x: float(math.factorial(int(x)))),      # type: ignore[arg-type]
            "8": ("绝对值 |x|", lambda x: abs(x)),
        }
        print("\n科学计算功能:")
        for k, (name, _) in ops.items():
            print(f"  {k}. {name}")

        op_choice = input("请选择 (1-8): ").strip()
        if op_choice not in ops:
            print("⚠️ 无效选择！")
            return

        try:
            x = float(input("请输入数值: ").strip())
            name, func = ops[op_choice]
            result = func(x)
            self.result = result
            expr = f"{name.split()[1]}({x}) = {result}"
            self.history.append(expr)
            print(f"📝 {expr}")
        except ValueError as e:
            print(f"❌ 错误: {e}")

    def _base_converter(self) -> None:
        """进制转换"""
        print("\n进制转换:")
        print("  1. 十进制 → 二进制")
        print("  2. 十进制 → 八进制")
        print("  3. 十进制 → 十六进制")
        print("  4. 二进制 → 十进制")
        print("  5. 十六进制 → 十进制")

        choice = input("请选择 (1-5): ").strip()
        try:
            if choice == "1":
                n = int(input("输入十进制数: ").strip())
                print(f"📝 二进制: {bin(n)}")
                self.history.append(f"{n}(10) → {bin(n)}(2)")
            elif choice == "2":
                n = int(input("输入十进制数: ").strip())
                print(f"📝 八进制: {oct(n)}")
                self.history.append(f"{n}(10) → {oct(n)}(8)")
            elif choice == "3":
                n = int(input("输入十进制数: ").strip())
                print(f"📝 十六进制: {hex(n)}")
                self.history.append(f"{n}(10) → {hex(n)}(16)")
            elif choice == "4":
                s = input("输入二进制数 (如 1010): ").strip()
                n = int(s, 2)
                print(f"📝 十进制: {n}")
                self.history.append(f"{s}(2) → {n}(10)")
            elif choice == "5":
                s = input("输入十六进制数 (如 FF): ").strip()
                n = int(s, 16)
                print(f"📝 十进制: {n}")
                self.history.append(f"{s}(16) → {n}(10)")
            else:
                print("⚠️ 无效选择！")
        except ValueError:
            print("❌ 输入格式错误！")

    def _show_history(self) -> None:
        """显示历史记录"""
        if not self.history:
            print("📭 暂无历史记录。")
            return
        print("\n📋 计算历史:")
        for i, record in enumerate(self.history, 1):
            print(f"  {i}. {record}")


# ============================================================
# 主程序入口
# ============================================================
if __name__ == "__main__":
    calc = Calculator()
    calc.interactive_menu()
