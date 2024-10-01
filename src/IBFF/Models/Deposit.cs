
namespace IBFF.Models;

public class Deposit : Operation
{
    public float Amount { get; set; }

    public Deposit(Operation p_operation, float p_amount)
    {
        Id = p_operation.Id;
        Deleted = p_operation.Deleted;
        InsertDate = p_operation.InsertDate;
        UpdateDate = p_operation.UpdateDate;
        OperationType = OperationType.Deposit;
        Portfolio = p_operation.Portfolio;

        Amount = p_amount;
    }
}

