using IBFF.Models;
using IBFF.Utilities;

namespace IBFF.Validators;

public class WithdrawCommand : IOperationCommand
{
    private Portfolio _portfolio;
    private float _amount;

    public WithdrawCommand(Withdraw p_withdraw)
    {
        _portfolio = p_withdraw.Portfolio;
        _amount = p_withdraw.Amount;
    }

    public void Execute()
    {
        _portfolio.Deposit -= _amount;
        _portfolio.Cash -= _amount;
        _portfolio.Value -= _amount;
    }

    public void Undo()
    {
        _portfolio.Deposit += _amount;
        _portfolio.Cash += _amount;
        _portfolio.Value += _amount;
    }

    public bool Validate()
    {
        return !FloatingPointComparison.LessThan(_portfolio.Deposit, 0f) && !FloatingPointComparison.LessThan(_portfolio.Cash, 0f);
    }
}

