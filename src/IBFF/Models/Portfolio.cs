
namespace IBFF.Models;

public class Portfolio
{
    public int Id { get; set; }
    public bool Deleted { get; set; }
    public DateTime InsertDate { get; set; }
    public DateTime UpdateDate { get; set; }

    public float Deposit { get; set; }
    public float Cash { get; set; }
    public float Value { get; set; }

    public PriorityQueue<Operation, DateTime> Operations { get; set; } = new PriorityQueue<Operation, DateTime>();
}

