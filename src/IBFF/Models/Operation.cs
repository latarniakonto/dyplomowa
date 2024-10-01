
namespace IBFF.Models;

public enum OperationType
{
    Deposit = 0,
    Withdraw,
    Transaction,
    Dividend,
    Split
}

public class Operation
{
    public int Id { get; set; }
    public bool Deleted { get; set; }
    public DateTime InsertDate { get; set; }
    public DateTime UpdateDate { get; set; }

    public OperationType OperationType { get; set; }
    public Portfolio Portfolio { get; set; } = new Portfolio();
}

