using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using IBFF.Models;

namespace IBFF.Controllers;

public class PortfolioController : Controller
{

    public PortfolioController()
    {
    }

    public IActionResult Index()
    {
        return View();
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}

