build:
	dotnet build

test:
	dotnet test

clean:
	dotnet clean

restore:
	dotnet restore

watch:
	dotnet watch --project src/IBFF/IBFF.csproj run

start:
	dotnet run --project src/IBFF/IBFF.csproj
