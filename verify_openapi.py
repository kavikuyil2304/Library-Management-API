
import sys
from fastapi.routing import APIRoute
from main import app


def verify_openapi():
    # Actual API routes registered in FastAPI
    actual_routes = set()

    for route in app.routes:
        if isinstance(route, APIRoute) and route.include_in_schema:
            for method in route.methods or []:
                if method not in {"HEAD", "OPTIONS"}:
                    actual_routes.add((route.path, method.upper()))

    # Routes documented in OpenAPI
    openapi_schema = app.openapi()
    documented_routes = set()

    for path, methods in openapi_schema["paths"].items():
        for method in methods:
            documented_routes.add((path, method.upper()))

    # Compare both sets
    missing_in_docs = actual_routes - documented_routes
    missing_in_api = documented_routes - actual_routes

    print("\n===== OPENAPI VERIFICATION =====")

    if not missing_in_docs and not missing_in_api:
        print("SUCCESS: All API routes match OpenAPI documentation!")
        print(f"Verified endpoints: {len(actual_routes)}")
        return True

    if missing_in_docs:
        print("\nRoutes missing in OpenAPI documentation:")
        for path, method in sorted(missing_in_docs):
            print(f"{method} {path}")

    if missing_in_api:
        print("\nRoutes documented but not registered in API:")
        for path, method in sorted(missing_in_api):
            print(f"{method} {path}")

    print("\nFAILED: OpenAPI verification found mismatches.")
    return False


if __name__ == "__main__":
    if not verify_openapi():
        sys.exit(1)
