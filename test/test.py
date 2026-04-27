import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_adder(dut):

    # -------------------------
    # Init
    # -------------------------
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.ena.value = 1
    dut.clk.value = 0
    dut.rst_n.value = 1   # not used, keep high

    await Timer(10, units="ns")

    # -------------------------
    # Test multiple cases
    # -------------------------
    for a in range(16):
        for b in range(16):

            # Pack inputs: b in upper 4 bits, a in lower 4 bits
            dut.ui_in.value = (b << 4) | a

            await Timer(1, units="ns")  # allow settle

            result = dut.uo_out.value.integer & 0x1F  # 5-bit result
            expected = a + b

            print(f"A={a}, B={b}, SUM={result}, EXPECTED={expected}")

            assert result == expected, f"Mismatch: {a}+{b} != {result}"

    # -------------------------
    # Test disable (ena = 0)
    # -------------------------
    dut.ena.value = 0
    dut.ui_in.value = (5 << 4) | 3  # 5 + 3

    await Timer(1, units="ns")

    result = dut.uo_out.value.integer
    print(f"Disable check: output={result}")

    assert result == 0, "Output should be 0 when ena=0"

    print("PASS ✅")
