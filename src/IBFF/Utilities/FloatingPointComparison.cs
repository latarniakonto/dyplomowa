
namespace IBFF.Utilities;

public static class FloatingPointComparison
{
    private const float EPSILON = 1e-05f;

    public static bool AreClose(float p_value1, float p_value2)
    {
        if (p_value1 == p_value2)
            return true;

        float value1 = Math.Abs(p_value1);
        float value2 = Math.Abs(p_value2);
        float diff = Math.Abs(p_value1 - p_value2);

        if (p_value1 == 0 || p_value2 == 0 || value1 + value2 < float.MinValue)
        {
            return diff < (EPSILON * float.MinValue);
        }
        else
        {
            return diff / (value1 + value2) < EPSILON;
        }
    }

    public static bool LessThan(float p_value1, float p_value2)
    {
        if (p_value1 < p_value2)
            return !FloatingPointComparison.AreClose(p_value1, p_value2);

        return false;
    }
}

