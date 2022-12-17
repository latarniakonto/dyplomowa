import { appToast } from "@/main";

export function toastSuccess(detail: string, life: number) {
  appToast.add({
    severity: "success",
    summary: "Success",
    detail: detail,
    life: life,
  });
}

export function toastError(detail: string, life: number) {
  appToast.add({
    severity: "error",
    summary: "Error",
    detail: detail,
    life: life,
  });
}
