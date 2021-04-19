package models

type Card struct {
	Title   string `json:"title"`
	UserID  int    `json:"user_id"`
	BoardID int    `json:"board_id"`
}
