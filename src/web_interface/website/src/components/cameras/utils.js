// https://stackoverflow.com/a/10284006
export const zip = (...rows) =>
    [...rows[0]].map((_, c) => rows.map((row) => row[c]))
