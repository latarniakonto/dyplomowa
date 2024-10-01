
namespace IBFF.Models;

public class Withdraw : Operation
{
    public float Amount { get; set; }

    public Withdraw(Operation p_operation, float p_amount)
    {
        Id = p_operation.Id;
        Deleted = p_operation.Deleted;
        InsertDate = p_operation.InsertDate;
        UpdateDate = p_operation.UpdateDate;
        OperationType = OperationType.Withdraw;
        Portfolio = p_operation.Portfolio;

        Amount = p_amount;
    }
}

