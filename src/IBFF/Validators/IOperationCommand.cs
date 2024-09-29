
namespace IBFF.Validators;

public interface IOperationCommand
{
    bool Validate();
    void Execute();
    void Undo();
}

