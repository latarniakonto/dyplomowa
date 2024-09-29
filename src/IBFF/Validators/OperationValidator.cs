using IBFF.Models;

namespace IBFF.Validators;

public class OperationValidator
{
    public bool ValidateCreating(Operation p_operation)
    {
        if (p_operation == null)
            throw new ArgumentNullException();

        if (p_operation.Portfolio == null)
            throw new InvalidOperationException("Performing an operation in detached portfolio state");

        Portfolio newPortfolio = new Portfolio();
        PriorityQueue<Operation, DateTime> operationsToApply = p_operation.Portfolio.Operations;
        operationsToApply.Enqueue(p_operation, DateTime.Now);

        while (operationsToApply.Count > 0)
        {
            Operation operation = operationsToApply.Dequeue();
            operation.Portfolio = newPortfolio;
            IOperationCommand operationCommand = GetOperationCommand(operation);

            operationCommand.Execute();

            if (!operationCommand.Validate())
                return false;
        }

        p_operation.Portfolio = newPortfolio;
        return true;
    }

    public bool ValidateDeleting(Operation p_operation)
    {
        if (p_operation == null)
            throw new ArgumentNullException();

        if (p_operation.Portfolio == null)
            throw new InvalidOperationException("Performing an operation in detached portfolio state");

        Portfolio newPortfolio = new Portfolio();
        PriorityQueue<Operation, DateTime> operationsToApply = p_operation.Portfolio.Operations;

        while (operationsToApply.Count > 0)
        {
            Operation operation = operationsToApply.Dequeue();
            if (System.Object.ReferenceEquals(operation, p_operation))
                continue;

            operation.Portfolio = newPortfolio;
            IOperationCommand operationCommand = GetOperationCommand(operation);

            operationCommand.Execute();

            if (!operationCommand.Validate())
                return false;
        }

        p_operation.Portfolio = newPortfolio;
        return true;
    }

    IOperationCommand GetOperationCommand(Operation p_operation)
    {
        switch (p_operation)
        {
            case Deposit deposit:
                return new DepositCommand((Deposit)p_operation);

            case Withdraw withdraw:
                return new WithdrawCommand((Withdraw)p_operation);
            default:
                throw new ArgumentException("An unrecognized operation type");
        }
    }
}

