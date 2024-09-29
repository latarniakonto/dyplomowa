using IBFF.Models;
using IBFF.Utilities;

namespace IBFF.Validators;

public class DepositCommand : IOperationCommand
{
    private Portfolio _portfolio;
    private float _amount;

    public DepositCommand(Deposit p_deposit)
    {
        _portfolio = p_deposit.Portfolio;
        _amount = p_deposit.Amount;
    }

    public void Execute()
    {
        _portfolio.Deposit += _amount;
        _portfolio.Cash += _amount;
        _portfolio.Value += _amount;
    }

    public void Undo()
    {
        _portfolio.Deposit -= _amount;
        _portfolio.Cash -= _amount;
        _portfolio.Value -= _amount;
    }

    public bool Validate()
    {
        return !FloatingPointComparison.LessThan(_portfolio.Deposit, 0f) && !FloatingPointComparison.LessThan(_portfolio.Cash, 0f);
    }
}

